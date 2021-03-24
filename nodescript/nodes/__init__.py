import sys
import bpy
from functools import partial

from nodescript.type_system import *
from nodescript.nodes.Base import *
from nodescript.nodes.types import *
from nodescript.nodes.shader import *
from nodescript.nodes.math import *
from nodescript.nodes.vmath import *
from nodescript.nodes.group import *


def get_node_func(name: str, mode: GraphMode):
    for module_name in ["types", "group", mode.value]:
        module = __name__ + "." + module_name
        if hasattr(sys.modules[module], name):
            cls = getattr(sys.modules[module], name)
            return partial(cls, mode=mode)
    for g in bpy.data.node_groups:
        print(name, g.name, mode.value, g.type.lower())
        if g.name == name and g.type.lower() == mode.value:
            f = Group.from_name(name, mode)
            print(f)
            return f
