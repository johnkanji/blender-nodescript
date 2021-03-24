import bpy
from typing import Dict

from . import NodeBase
from ..type_system import *


class Group(NodeBase):
    _inputs: Dict[str, BType]
    _outputs: Dict[str, BType]
    _mode: str
    _group: any

    def __init__(self, params: Dict[str, Value], mode: GraphMode):
        self._mode = mode
        name = [p for p in params if p[0] == "name"][0]
        params.remove(name)
        assert name[1].btype == BType.STRING

        self._group = bpy.data.node_groups.get(name[1].value)
        self._inputs = {
            inp.name: BType(inp.type.capitalize()) for inp in self._group.inputs
        }
        self._outputs = {
            out.name: BType(out.type.capitalize()) for out in self._group.outputs
        }
        super(Group, self).__init__(params)

    @classmethod
    def from_name(cls, name: str, mode: GraphMode):
        def constr(params):
            params.append(("name", Value(name, BType.STRING)))
            return cls(params, mode)

        return constr

    @property
    def bnode(self):
        return f"{self._mode.value.capitalize()}NodeGroup"

    @property
    def inputs(self):
        return self._inputs

    @property
    def outputs(self):
        return self._outputs

    @property
    def translation(self):
        return {
            **{inp.name: inp.identifier.lower() for inp in self._group.inputs},
            **{out.name: out.identifier.lower() for out in self._group.outputs},
        }

    def after_add(self, bnode):
        bnode.node_tree = self._group


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