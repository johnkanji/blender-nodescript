import bpy
from . import parse


class NodescriptCompile(bpy.types.Operator):
    """Compile Nodescript into Blender NodeTree"""
    bl_idname = "nodescript.compile"
    bl_label = "Compile"
    bl_options = {'UNDO'}

    def execute(self, context):
        # clss = [c for c in dir(bpy.types) if 'ShaderNode' in c and c != 'ShaderNode']
        # inherited = list(dir(bpy.types.NodeInternal))
        # print(dir(bpy.types.ShaderNodeVectorMath))
        # print(inherited)
        # for c in clss:
        #     cls = getattr(bpy.types, c)
        #     # if not hasattr(cls, 'input_template') and not hasattr(cls, 'output_template'):
        #     #     print(cls)
        #     print(cls)
        #     for a in dir(cls):
        #         if a not in inherited:
        #             print(' ', a)
        parse.main()

        return {'FINISHED'}
