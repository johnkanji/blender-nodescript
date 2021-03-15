import sys

from nodescript.type_system import *
from nodescript.nodes.Base import *
from nodescript.nodes.shader_color import *
from nodescript.nodes.shader_converter import *
from nodescript.nodes.shader_input import *
from nodescript.nodes.shader_output import *
from nodescript.nodes.shader_shader import *
from nodescript.nodes.shader_texture import *
from nodescript.nodes.shader_vector import *
from nodescript.nodes.math import *
from nodescript.nodes.vmath import *


class Vector(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeVectorMath'
    
    @property
    def inputs(self):
        return {
            'x': BType.VALUE,
            'y': BType.VALUE,
            'z': BType.VALUE
        }
    
    @property
    def outputs(self):
        return {
            'vector': BType.VECTOR
        }
        
    def after_add(self, bnode):
        bnode.inputs[0].default_value[0] = self.params['x'].value
        bnode.inputs[0].default_value[1] = self.params['y'].value
        bnode.inputs[0].default_value[2] = self.params['z'].value
        bnode.label = 'Vector'
        bnode.inputs[1].hide = True
        bnode.show_options = False
        bnode.hide = True
        


def get_node_func(name: str, mode: GraphMode) -> NodeBase:
    try:
        cls = getattr(sys.modules[__name__], name)
        return cls
    except AttributeError:
        raise NameError(f'node \'{name}\' is not defined')


if __name__ == '__main__':
    v = Vector()
    print(v.ntype)