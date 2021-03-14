from abc import ABC, abstractmethod
from uuid import UUID, uuid4
from typing import Dict

from nodescript.type_system import *

class NodeBase(ABC):

    btype = BType.NODE
    layer = 0
    id: UUID

    @property
    def ntype(self):
        return type(self).__name__
    
    @property
    @abstractmethod
    def bnode(self):
        pass

    @property
    @abstractmethod
    def inputs(self) -> Dict[str, BType]:
        pass

    @property
    @abstractmethod
    def outputs(self) -> Dict[str, BType]:
        pass

    @property
    def translation(self) -> Dict[str, str]:
        pass

    def __init__(self, params=None):
        self.id = uuid4()

        if params is None:
            params = {}
        args = {}
        inputs = list(self.inputs.items())
        for i, (k, v) in enumerate(params):
            vtype = v.btype
            if k is None:
                k = inputs[i][0]
            if isinstance(v, Variable):
                v = v.value
            if v.btype == BType.NODE:
                vout = list(v.outputs.items())[0]
                v = Value(vout[0], vout[1], v.id)
            assert vtype == self.inputs[k] or v.btype == self.inputs[k],\
                f'invalid type for parameter \'{k}\' {v.btype}'
            args[k] = v
        self.params = args

        # print('new node', self.ntype, self.id)
        # for k, v in self.params.items():
        #     print(' ', k, v)
        # print()

    def access(self, name):
        assert name in self.outputs.keys(),\
            f'node {self.ntype} has no output {name}'
        return Value(name, self.outputs[name], self.id)
    
    def translate_name(self, name):
        try:
            translated_name = self.translation[name]
        except (KeyError, TypeError):
            translated_name = name
        return translated_name

    def __repr__(self):
        return f'Node({self.ntype})'
    

class Namespace(ABC):

    @property
    def ntype(self):
        return type(self).__name__
    
    @property
    @abstractmethod
    def nodes(self):
        pass
    
    def access(self, name):
        assert name in self.nodes.keys(),\
            f'namespace {self.ntype} has no output {name}'
        return Value(self.nodes[name], BType.NODE_FUNC)