from ..type_system import *
from nodescript.nodes import NodeBase, Namespace


def _after_add_func(op):
    def func(self, bnode):
        bnode.show_options = False
        bnode.operation = op

    return func


class Math(Namespace):
    class _MathBase(NodeBase):
        @property
        def bnode(self):
            return "ShaderNodeMath"

        @property
        def outputs(self):
            return {"value": BType.VALUE}

        @property
        def translation(self):
            return {
                "value1": "value",
                "value2": "value_001",
                "value3": "value_002",
            }

    class _UnOp(_MathBase):
        @property
        def inputs(self):
            return {
                "value": BType.VALUE,
                "clamp": BType.BOOL,
            }

    class _BinOp(_MathBase):
        @property
        def inputs(self):
            return {
                "value1": BType.VALUE,
                "value2": BType.VALUE,
                "clamp": BType.BOOL,
            }

    class Add(_BinOp):
        after_add = _after_add_func("ADD")

    class Sub(_BinOp):
        after_add = _after_add_func("SUBTRACT")

    class Mul(_BinOp):
        after_add = _after_add_func("MULTIPLY")

    class Div(_BinOp):
        after_add = _after_add_func("DIVIDE")

    class Pow(_MathBase):
        @property
        def inputs(self):
            return {
                "base": BType.VALUE,
                "exponent": BType.VALUE,
                "clamp": BType.BOOL,
            }

        after_add = _after_add_func("POWER")

    class Log(_MathBase):
        @property
        def inputs(self):
            return {
                "value": BType.VALUE,
                "base": BType.VALUE,
                "clamp": BType.BOOL,
            }

        after_add = _after_add_func("LOGARITHM")

    class Sqrt(_UnOp):
        after_add = _after_add_func("SQRT")

    class InvSqrt(_UnOp):
        after_add = _after_add_func("INVERSE_SQRT")

    class Abs(_UnOp):
        after_add = _after_add_func("ABSOLUTE")

    class Exp(_UnOp):
        after_add = _after_add_func("EXPONENT")

    class Min(_BinOp):
        after_add = _after_add_func("MINIMUM")

    class Max(_BinOp):
        after_add = _after_add_func("MAXIMUM")

    class Lesser(_BinOp):
        after_add = _after_add_func("LESS_THAN")

    class Greater(_BinOp):
        after_add = _after_add_func("GREATER_THAN")

    class Sign(_UnOp):
        after_add = _after_add_func("SIGN")

    class Compare(_MathBase):
        @property
        def inputs(self):
            return {
                "value1": BType.VALUE,
                "value2": BType.VALUE,
                "epsilon": BType.VALUE,
                "clamp": BType.BOOL,
            }

        after_add = _after_add_func("COMPARE")

    class SmoothMin(_MathBase):
        @property
        def inputs(self):
            return {
                "value1": BType.VALUE,
                "value2": BType.VALUE,
                "distance": BType.VALUE,
                "clamp": BType.BOOL,
            }

        after_add = _after_add_func("SMOOTH_MIN")

    class SmoothMax(_MathBase):
        @property
        def inputs(self):
            return {
                "value1": BType.VALUE,
                "value2": BType.VALUE,
                "distance": BType.VALUE,
                "clamp": BType.BOOL,
            }

        after_add = _after_add_func("SMOOTH_MAX")

    class Round(_UnOp):
        after_add = _after_add_func("ROUND")

    class Floor(_UnOp):
        after_add = _after_add_func("FLOOR")

    class Ceil(_UnOp):
        after_add = _after_add_func("CEIL")

    class Truncate(_UnOp):
        after_add = _after_add_func("TRUNC")

    class Fraction(_UnOp):
        after_add = _after_add_func("FRACT")

    class Mod(_BinOp):
        after_add = _after_add_func("MODULO")

    class Wrap(_MathBase):
        @property
        def inputs(self):
            return {
                "value": BType.VALUE,
                "min": BType.VALUE,
                "max": BType.VALUE,
                "clamp": BType.BOOL,
            }

        after_add = _after_add_func("WRAP")

    class Snap(_MathBase):
        @property
        def inputs(self):
            return {
                "value": BType.VALUE,
                "increment": BType.VALUE,
                "clamp": BType.BOOL,
            }

        after_add = _after_add_func("SNAP")

    class PingPong(_MathBase):
        @property
        def inputs(self):
            return {
                "value": BType.VALUE,
                "scale": BType.VALUE,
                "clamp": BType.BOOL,
            }

        after_add = _after_add_func("PINGPONG")

    class Sin(_UnOp):
        after_add = _after_add_func("SINE")

    class Cos(_UnOp):
        after_add = _after_add_func("COSINE")

    class Tan(_UnOp):
        after_add = _after_add_func("TANGENT")

    class Asin(_UnOp):
        after_add = _after_add_func("ARCSINE")

    class Acos(_UnOp):
        after_add = _after_add_func("ARCCOSINE")

    class Atan(_UnOp):
        after_add = _after_add_func("ARCTANGENT")

    class Atan2(_BinOp):
        after_add = _after_add_func("ARCTAN2")

    class Sinh(_UnOp):
        after_add = _after_add_func("SINH")

    class Cosh(_UnOp):
        after_add = _after_add_func("COSH")

    class Tanh(_UnOp):
        after_add = _after_add_func("TANH")

    class ToRad(_UnOp):
        after_add = _after_add_func("RADIANS")

    class ToDeg(_UnOp):
        after_add = _after_add_func("DEGREES")
