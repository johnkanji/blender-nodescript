from ..type_system import *
from nodescript.nodes import NodeBase, Namespace


def _after_add_func(op):
    def func(self, bnode):
        bnode.show_options = False
        bnode.operation = op
    return func

class VMath(Namespace):
    class _VMathBase(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'

        @property
        def outputs(self):
            return {
                'vector': BType.VECTOR
            }

        @property
        def translation(self):
            return {
                'vector1': 'vector',
                'vector2': 'vector_001',
                'vector3': 'vector_002'
            }

    class _UnOp(_VMathBase):
        @property
        def inputs(self):
            return {
                'vector': BType.VECTOR
            }

    class _BinOp(_VMathBase):
        @property
        def inputs(self):
            return {
                'vector1': BType.VECTOR,
                'vector2': BType.VECTOR
            }


    class Add(_BinOp):
        after_add = _after_add_func('ADD')

    class Sub(_BinOp):
        after_add = _after_add_func('SUBTRACT')

    class Mul(_BinOp):
        after_add = _after_add_func('MULTIPLY')

    class Div(_BinOp):
        after_add = _after_add_func('DIVIDE')

    class Cross(_BinOp):
        after_add = _after_add_func('CROSS_PRODUCT')

    class Project(_BinOp):
        after_add = _after_add_func('PROJECT')

    class Reflect(_BinOp):
        after_add = _after_add_func('REFLECT')

    class Dot(_BinOp):
        @property
        def outputs(self):
            return {
                'value': BType.VALUE
            }
        after_add = _after_add_func('DOT_PRODUCT')

    class Distance(_BinOp):
        @property
        def outputs(self):
            return {
                'value': BType.VALUE
            }
        after_add = _after_add_func('DISTANCE')

    class Length(_UnOp):
        @property
        def outputs(self):
            return {
                'value': BType.VALUE
            }
        after_add = _after_add_func('LENGTH')

    class Scale(_VMathBase):
        @property
        def inputs(self):
            return {
                'vector': BType.VECTOR,
                'scale': BType.VALUE
            }
        after_add = _after_add_func('SCALE')

    class Normalize(_UnOp):
        after_add = _after_add_func('NORMALIZE')

    class Abs(_UnOp):
        after_add = _after_add_func('ABSOLUTE')

    class Min(_BinOp):
        after_add = _after_add_func('MINIMUM')

    class Max(_BinOp):
        after_add = _after_add_func('MAXIMUM')

    class Floor(_UnOp):
        after_add = _after_add_func('FLOOR')

    class Ceil(_UnOp):
        after_add = _after_add_func('CEIL')

    class Fraction(_UnOp):
        after_add = _after_add_func('FRACTION')

    class Mod(_BinOp):
        after_add = _after_add_func('MODULO')

    class Wrap(_VMathBase):
        @property
        def inputs(self):
            return {
                'vector': BType.VECTOR,
                'min': BType.VECTOR,
                'max': BType.VECTOR
            }
        @property
        def translation(self):
            return {
                'max': 'vector_001',
                'min': 'vector_002'
            }
        after_add = _after_add_func('WRAP')

    class Snap(_VMathBase):
        @property
        def inputs(self):
            return {
                'vector': BType.VECTOR,
                'increment': BType.VECTOR
            }
        @property
        def translation(self):
            return {
                'increment': 'vector_001'
            }
        after_add = _after_add_func('SNAP')

    class Sin(_UnOp):
        after_add = _after_add_func('SINE')

    class Cos(_UnOp):
        after_add = _after_add_func('COSINE')

    class Tan(_UnOp):
        after_add = _after_add_func('TANGENT')