from .. import NodeBase
from ...type_system import *


class Bump(NodeBase):
    @property
    def bnode(self):
        return "ShaderNodeBump"

    @property
    def inputs(self):
        return {
            "invert": BType.BOOL,
            "strength": BType.VALUE,
            "distance": BType.VALUE,
            "height": BType.VALUE,
            "normal": BType.VECTOR,
        }

    @property
    def outputs(self):
        return {"normal": BType.VECTOR}


class Displacement(NodeBase):
    @property
    def bnode(self):
        return "ShaderNodeDisplacement"

    @property
    def inputs(self):
        return {
            "space": BType.STRING,
            "height": BType.VALUE,
            "midlevel": BType.VALUE,
            "scale": BType.VALUE,
            "normal": BType.VECTOR,
        }

    @property
    def outputs(self):
        return {"displacement": BType.VECTOR}


class Mapping(NodeBase):
    @property
    def bnode(self):
        return "ShaderNodeMapping"

    @property
    def inputs(self):
        return {
            "type": BType.STRING,
            "vector": BType.VECTOR,
            "location": BType.VECTOR,
            "rotation": BType.VECTOR,
            "scale": BType.VECTOR,
        }

    @property
    def outputs(self):
        return {"vector": BType.VECTOR}

    @property
    def translation(self):
        return {"type": "vector_type"}


class Normal(NodeBase):
    @property
    def bnode(self):
        return "ShaderNodeNormal"

    @property
    def inputs(self):
        return {"normal": BType.VECTOR}

    @property
    def outputs(self):
        return {"normal": BType.VECTOR, "dot": BType.VALUE}


class NormalMap(NodeBase):
    @property
    def bnode(self):
        return "ShaderNodeNormalMap"

    @property
    def inputs(self):
        return {"space": BType.STRING, "strength": BType.VALUE, "color": BType.COLOR}

    @property
    def outputs(self):
        return {"normal": BType.VECTOR}


class VectorCurves(NodeBase):
    @property
    def bnode(self):
        return "ShaderNodeVectorCurve"

    @property
    def inputs(self):
        return {"fac": BType.VALUE, "vector": BType.VECTOR}

    @property
    def outputs(self):
        return {"vector": BType.VECTOR}


class VectorCurves(NodeBase):
    @property
    def bnode(self):
        return "ShaderNodeVectorDisplacement"

    @property
    def inputs(self):
        return {
            "space": BType.STRING,
            "vector": BType.VECTOR,
            "midlevel": BType.VALUE,
            "scale": BType.VALUE,
        }

    @property
    def outputs(self):
        return {"displacement": BType.VECTOR}


class VectorRotate(NodeBase):
    @property
    def bnode(self):
        return "ShaderNodeVectorRotate"

    @property
    def inputs(self):
        return {
            "type": BType.STRING,
            "invert": BType.BOOL,
            "vector": BType.VECTOR,
            "center": BType.VECTOR,
            "axis": BType.VECTOR,
            "angle": BType.VALUE,
        }

    @property
    def outputs(self):
        return {"vector": BType.VECTOR}

    @property
    def translation(self):
        return {"type": "rotation_type"}


class VectorTransform(NodeBase):
    @property
    def bnode(self):
        return "ShaderNodeVectorTransform"

    @property
    def inputs(self):
        return {
            "type": BType.STRING,
            "convert_from": BType.STRING,
            "convert_from": BType.STRING,
            "vector": BType.VECTOR,
        }

    @property
    def outputs(self):
        return {"vector": BType.VECTOR}

    @property
    def translation(self):
        return {"type": "vector_type"}
