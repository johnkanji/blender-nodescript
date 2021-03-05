from . import NodeBase
from ..type_system import *


class AOVOutput(NodeBase):
    @property
    def inputs(self):
        return {
            'name': BType.STRING,
            'color': BType.COLOR,
            'value': BType.VALUE
        }

    @property
    def outputs(self):
        return {}

class MaterialOutput(NodeBase):
    @property
    def inputs(self):
        return {
            'target': BType.STRING,
            'surface': BType.SHADER,
            'volume': BType.SHADER,
            'displacement': BType.VECTOR
        }

    @property
    def outputs(self):
        return {}