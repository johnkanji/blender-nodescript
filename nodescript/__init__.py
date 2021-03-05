# flake8: noqa: F821, F722

bl_info = {
    "name": "Nodescript",
    "blender": (2, 92, 0),
    "category": "Development",
}

import os
import sys

mpath = os.path.dirname(os.path.realpath(__file__))
if not any(mpath in v for v in sys.path):
    sys.path.insert(0, mpath)

if 'bpy' in locals():
    import importlib
    importlib.reload(operators)
    importlib.reload(ui)
else:
    import bpy
    from . import (operators, ui, type_system, nodes)


classes = (
    operators.NodescriptCompile,
    ui.NodescriptPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
