from .. import NodeBase
from ...type_system import *


class Vector(NodeBase):
    @property
    def bnode(self):
        return "ShaderNodeVectorMath"

    @property
    def inputs(self):
        return {"x": BType.VALUE, "y": BType.VALUE, "z": BType.VALUE}

    @property
    def outputs(self):
        return {"vector": BType.VECTOR}

    def after_add(self, bnode):
        bnode.inputs[0].default_value[0] = self.params["x"].value
        bnode.inputs[0].default_value[1] = self.params["y"].value
        bnode.inputs[0].default_value[2] = self.params["z"].value
        bnode.label = "Vector"
        bnode.inputs[1].hide = True
        bnode.show_options = False
        bnode.hide = True