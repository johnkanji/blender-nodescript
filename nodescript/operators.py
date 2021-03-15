import bpy
from . import parse


class NodescriptCompile(bpy.types.Operator):
    """Compile Nodescript into Blender NodeTree"""
    bl_idname = "nodescript.compile"
    bl_label = "Compile"
    bl_options = {'UNDO'}

    def execute(self, context):
        parser = parse.parse(bpy.context.edit_text.as_string().strip())
        print('PARSE DONE')
        print('Graph type:', parser.mode)
        print('Tree Name:', parser.name)
        for k, n in parser.nodes.items():
            print(n, k)
            for a, p in n.params.items():
                print(' ', a, p)

        mat_name = parser.name
        mat = (bpy.data.materials.get(mat_name) or
               bpy.data.materials.new(mat_name))
        mat.use_nodes = True

        tree = mat.node_tree
        for node in tree.nodes:
            tree.nodes.remove(node)

        id_to_bnode = self.to_bnodes(parser.nodes, tree)
        self.layout_nodes(parser.nodes, id_to_bnode)

        return {'FINISHED'}

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

    def get_node_socket(self, sockets, name):
        for sock in sockets:
            if sock.identifier.lower() == name:
                return sock

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