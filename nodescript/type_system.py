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
class Variable:
    name: str
    value: any
    btype: BType = None

    def __repr__(self):
        return f"Var({self.name}, {self.value}, {self.btype})"


@dataclass
class Value:
    value: any
    btype: BType
    node_id: UUID = None

    def __repr__(self):
        nid = f", {self.node_id }" if self.node_id is not None else ""
        return f"Value({self.value}, {self.btype}{nid})"


@dataclass
class Tree(object):
    name: str
    mode: GraphMode
    is_func: bool
    nodes: List[any]
