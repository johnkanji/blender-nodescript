from dataclasses import dataclass
from enum import Enum, auto
from uuid import UUID
from typing import List


class GraphMode(Enum):
    SHADER = "shader"
    COMPOSITING = "compositing"
    GEOMETRY = "geometry"


class BType(Enum):
    VALUE = "Value"
    VECTOR = "Vector"
    COLOR = "Color"
    NODE = "Node"
    STRING = "String"
    BOOL = "Boolean"
    SHADER = "Shader"
    NODE_FUNC = "NodeFunction"
    NAMESPACE = "Namespace"


@dataclass
class Value:
    value: any
    btype: BType
    node_id: UUID = None

    def get_value(self):
        return self

    def get_type(self):
        if self.btype == BType.NODE:
            return self.value.default().btype
        else:
            return self.btype

    def __repr__(self):
        nid = f", {self.node_id }" if self.node_id is not None else ""
        return f"Value({self.value}, {self.btype}{nid})"


@dataclass
class Variable:
    name: str
    value: Value
    btype: BType = None

    def get_value(self):
        return self.value

    def get_type(self):
        if self.btype is not None:
            return self.btype
        else:
            return self.value.get_type()

    def __repr__(self):
        return f"Var({self.name}, {self.value}, {self.btype})"


@dataclass
class Tree(object):
    name: str
    mode: GraphMode
    is_func: bool
    nodes: List[any]
