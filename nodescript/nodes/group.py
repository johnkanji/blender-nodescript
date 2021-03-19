from . import NodeBase
from ..type_system import *

class _GroupInput(NodeBase):
    def __init__(self, inps):
        self._inputs = inps
        super(_GroupInput, self).__init__()
    
    @property
    def bnode(self):
        return 'NodeGroupInput'
    
    @property
    def inputs(self):
        return {}

    @property
    def outputs(self):
        return self._inputs
    
class _GroupOutput(NodeBase):
    def __init__(self, outs, params):
        self._outputs = outs
        print('in _GroupOutput constr', params)
        super(_GroupOutput, self).__init__(params)
    
    @property
    def bnode(self):
        return 'NodeGroupInput'
    
    @property
    def inputs(self):
        return self._outputs

    @property
    def outputs(self):
        return {}