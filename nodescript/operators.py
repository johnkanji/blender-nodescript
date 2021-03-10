import bpy
from . import parse


class NodescriptCompile(bpy.types.Operator):
    """Compile Nodescript into Blender NodeTree"""
    bl_idname = "nodescript.compile"
    bl_label = "Compile"
    bl_options = {'UNDO'}

    def execute(self, context):
        nodes = parse.parse(parse.script)
        print('PARSE DONE')
        for node in nodes.values():
            print(node)
            for k, v in node.params.items():
                print(' ', k, v)
               
        mat_name = 'TestMat' 
        mat = (bpy.data.materials.get(mat_name) or 
               bpy.data.materials.new(mat_name))
        mat.use_nodes = True
        
        tree = mat.node_tree
        for node in tree.nodes:
            tree.nodes.remove(node)
            
        
        

        return {'FINISHED'}
