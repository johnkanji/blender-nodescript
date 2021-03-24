from . import NodeBase
from ..type_system import *


class _GroupInput(NodeBase):
    def __init__(self, inps):
        self._inputs = inps
        self._translation = {}
        super(_GroupInput, self).__init__()

    @property
    def bnode(self):
        return "NodeGroupInput"

    @property
    def inputs(self):
        return {}

    @property
    def outputs(self):
        return self._inputs

    @property
    def translation(self):
        return self._translation


class _GroupOutput(NodeBase):
    def __init__(self, outs, params):
        self._outputs = outs
        self._translation = {}
        super(_GroupOutput, self).__init__(params)

    @property
    def bnode(self):
        return "NodeGroupOutput"

    @property
    def inputs(self):
        return self._outputs

    @property
    def outputs(self):
        return {}

    @property
    def translation(self):
        return self._translation