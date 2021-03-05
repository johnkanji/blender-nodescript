import bpy

class NodescriptPanel(bpy.types.Panel):
    bl_idname = 'OBJECT_PT_Nodescript'
    bl_label = 'Nodescript'   # The name that will show up in the properties panel
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout

        layout.operator("nodescript.compile")