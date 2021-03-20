import bpy
from . import parse

from nodescript.type_system import BType, GraphMode, Tree


class NodescriptCompile(bpy.types.Operator):
    """Compile Nodescript into Blender NodeTree"""
    bl_idname = "nodescript.compile"
    bl_label = "Compile"
    bl_options = {'UNDO'}

    MODE_TO_TYPE = {
        GraphMode.SHADER: 'ShaderNodeTree',
        GraphMode.COMPOSITING: 'CompositorNodeTree'
    }

    BTYPE_TO_INOUT = {
        BType.VALUE: 'NodeSocketFloat',
        BType.VECTOR: 'NodeSocketVector',
        BType.COLOR: 'NodeSocketColor',
        BType.SHADER: 'NodeSocketShader',
    }

    def execute(self, context):
        for tree in parse.parse(bpy.context.edit_text.as_string().strip()):
            print('PARSE DONE')
            print('Graph type:', tree.mode, 'func' if tree.is_func else '')
            print('Tree Name:', tree.name)
            # for k, n in tree.nodes.items():
            #     print(n, k)
            #     for a, p in n.params.items():
            #         print(' ', a, p)
            print()

        btree = self.setup_tree(tree)
        if tree.is_func:
            self.setup_group_inout(tree, btree)

        id_to_bnode = self.to_bnodes(tree.nodes, btree)
        self.layout_nodes(tree.nodes, id_to_bnode)

        return {'FINISHED'}

    def setup_tree(self, tree: Tree):
        if tree.is_func:
            btree = (bpy.data.node_groups.get(tree.name) or
                    bpy.data.node_groups.new(tree.name, self.MODE_TO_TYPE[tree.mode]))
        else:
            if tree.mode == GraphMode.SHADER:
                obj = (bpy.data.materials.get(tree.name) or
                       bpy.data.materials.new(tree.name))
            elif tree.mode == GraphMode.COMPOSITING:
                obj = bpy.context.scene
            obj.use_nodes = True
            btree = obj.node_tree

        for node in btree.nodes:
            btree.nodes.remove(node)
        return btree

    def setup_group_inout(self, tree, btree):
        inp = next(filter(lambda n: n.bnode == 'NodeGroupInput', tree.nodes.values()))
        btree.inputs.clear()
        for p, t in inp._inputs.items():
            sock = btree.inputs.new(self.BTYPE_TO_INOUT[t], p)
            inp._translation[p] = sock.identifier.lower()

        out = next(filter(lambda n: n.bnode == 'NodeGroupOutput', tree.nodes.values()))
        btree.outputs.clear()
        for p, t in out._outputs.items():
            sock = btree.outputs.new(self.BTYPE_TO_INOUT[t], p)
            out._translation[p] = sock.identifier.lower()

    def to_bnodes(self, nodes, tree):
        bnodes = tree.nodes
        links = tree.links
        id_to_bnode = {}
        for node in nodes.values():
            bnode = bnodes.new(node.bnode)
            if hasattr(node, 'after_add'):
                node.after_add(bnode)
            id_to_bnode[node.id] = bnode

            for name, value in node.params.items():
                translated_name = node.translate_name(name)
                inp_sock = self.get_node_socket(bnode.inputs, translated_name)

                if value.node_id:
                    node_out = nodes[value.node_id]
                    bnode_out = id_to_bnode[value.node_id]
                    translated_name = node_out.translate_name(value.value)
                    out_sock = self.get_node_socket(bnode_out.outputs, translated_name)
                    links.new(inp_sock, out_sock)

                elif inp_sock:
                    inp_sock.default_value = value.value

        return id_to_bnode

    def layout_nodes(self, nodes, bnodes):
        HSPACE = 75
        VSPACE = 30

        for node in nodes.values():
            for p in node.params.values():
                if p.node_id:
                    node.layer = max(node.layer, nodes[p.node_id].layer + 1)

        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        nlayers = max([n.layer for n in nodes.values()])
        for i in range(nlayers + 1):
            layer_nodes = [n for n in nodes.values() if n.layer == i]
            for j in range(len(layer_nodes)):
                n = layer_nodes[j]
                b = bnodes[n.id]
                xpos = i* (140 + HSPACE)
                if j == 0:
                    b.location = (xpos, 0)
                else:
                    prev = bnodes[layer_nodes[j-1].id]
                    prev_bottom = prev.location[1] - prev.dimensions[1]/2
                    b.location = (xpos, prev_bottom - VSPACE)

    def get_node_socket(self, sockets, name):
        for sock in sockets:
            if sock.identifier.lower() == name:
                return sock