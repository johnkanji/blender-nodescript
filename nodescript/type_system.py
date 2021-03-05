from enum import Enum, auto
from uuid import UUID

class GraphMode(Enum):
    SHADER = auto()
    COMPOSITING = auto()
    GEOMETRY = auto()


class BType(Enum):
    VALUE = 'Value'
    VECTOR = 'Vector'
    COLOR = 'Color'
    NODE = 'Node'
    NODE_FUNC = 'NodeFunction'
    STRING = 'String'
    BOOL = 'Boolean'
    SHADER = 'Shader'
    NAMESPACE = 'Namespace'


class Variable:
    name: str = None
    value = None
    btype: BType = None
    node_id: UUID = None
    static: bool = False
    
    def __init__(self, name: str, value, btype: BType = None, static: bool = False):
        self.name = name
        self.value = value
        self.btype = btype
        self.static = static

    def __repr__(self):
        return f'Var({self.name}, {self.value}, {self.btype})'


class Value:
    value = None
    btype: BType = None
    node_id: UUID = None
    
    def __init__(self, value, btype, node_id: UUID = None):
        self.value = value
        self.btype = btype
        self.node_id = node_id

    def __repr__(self):
        nid = f', {self.node_id }' if self.node_id is not None else ''
        return f'Value({self.value}, {self.btype}{nid})'