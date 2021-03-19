from abc import ABC, abstractmethod
from uuid import UUID, uuid4
from typing import Dict
from inspect import isclass

from nodescript.type_system import *


class NodeBase(ABC):
    btype = BType.NODE
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
        self.layer = 0

        if params is None:
            params = {}
        args = {}
        inputs = list(self.inputs.items())
        for i, (k, v) in enumerate(params):
            if v.btype == BType.NODE:
                v = v.value.default()
            if k is None:
                k = inputs[i][0]
            assert v.btype == self.inputs[k],\
                f'invalid type for parameter \'{k}\' {v.btype}'
            args[k] = v
        self.params = args

    def access(self, name):
        assert name in self.outputs.keys(),\
            f'node {self.ntype} has no output {name}'
        return Value(name, self.outputs[name], self.id)
    
    def default(self):
        name = list(self.outputs.keys())[0]
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
    
    def access(self, name):
        assert name[0] != '_' and hasattr(self, name),\
            f'namespace {self.ntype} has no output {name}'
        attr = getattr(self, name)
        assert isclass(attr) and issubclass(attr, NodeBase),\
            f'namespace {self.ntype} has no output {name}'
        return Value(attr, BType.NODE_FUNC)