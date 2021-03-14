import sys
from abc import ABC, abstractmethod

from ..type_system import *
from nodescript.nodes import NodeBase, Namespace


def _after_add_func(op):
    def func(self, bnode):
        bnode.operation = op
    return func

class VMath(Namespace):
    
    @property
    def nodes(self):
        return {
            'Add': self.VAdd,
            'Sub': self.VSub,
            'Mul': self.VMul,
            'Div': self.VDiv,
            'Cross': self.VCross,
            'Project': self.VProject,
            'Reflect': self.VReflect,
            'Dot': self.VDot,
            'Distance': self.VDistance,
            'Length': self.VLength,
            'Scale': self.VScale,
            'Normalize': self.VNormalize,
            'Abs': self.VAbs,
            'Min': self.VMin,
            'Max': self.VMax
        }

    class VAdd(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'
        
        @property
        def inputs(self):
            return {
                'vector1': BType.VECTOR,
                'vector2': BType.VECTOR
            }

        @property
        def outputs(self):
            return {
                'vector': BType.VECTOR
            }
            
        @property
        def translation(self):
            return {
                'vector1': 'vector',
                'vector2': 'vector_001'
            }
            
        after_add = _after_add_func('ADD')
            
    class VSub(NodeBase):
        @property
        def inputs(self):
            return {
                'vector1': BType.VECTOR,
                'vector2': BType.VECTOR
            }

        @property
        def outputs(self):
            return {
                'vector': BType.VECTOR
            }
            
    class VMul(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'
        
        @property
        def inputs(self):
            return {
                'vector1': BType.VECTOR,
                'vector2': BType.VECTOR
            }

        @property
        def outputs(self):
            return {
                'vector': BType.VECTOR
            }
            
    class VDiv(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'
        
        @property
        def inputs(self):
            return {
                'vector1': BType.VECTOR,
                'vector2': BType.VECTOR
            }

        @property
        def outputs(self):
            return {
                'vector': BType.VECTOR
            }
            
    class VCross(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'
        
        @property
        def inputs(self):
            return {
                'vector1': BType.VECTOR,
                'vector2': BType.VECTOR
            }

        @property
        def outputs(self):
            return {
                'vector': BType.VECTOR
            }
            
    class VProject(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'
        
        @property
        def inputs(self):
            return {
                'vector1': BType.VECTOR,
                'vector2': BType.VECTOR
            }

        @property
        def outputs(self):
            return {
                'vector': BType.VECTOR
            }

    class VReflect(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'
        
        @property
        def inputs(self):
            return {
                'vector1': BType.VECTOR,
                'vector2': BType.VECTOR
            }

        @property
        def outputs(self):
            return {
                'vector': BType.VECTOR
            }
            
    class VDot(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'
        
        @property
        def inputs(self):
            return {
                'vector1': BType.VECTOR,
                'vector2': BType.VECTOR
            }

        @property
        def outputs(self):
            return {
                'value': BType.VALUE
            }
            
        @property
        def translation(self):
            return {
                'vector1': 'vector',
                'vector2': 'vector_001'
            }
            
        after_add = _after_add_func('DOT_PRODUCT')
    
    class VDistance(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'
        
        @property
        def inputs(self):
            return {
                'vector1': BType.VECTOR,
                'vector2': BType.VECTOR
            }

        @property
        def outputs(self):
            return {
                'vector': BType.VALUE
            }
            
    class VLength(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'
        
        @property
        def inputs(self):
            return {
                'vector': BType.VECTOR
            }

        @property
        def outputs(self):
            return {
                'vector': BType.VALUE
            }
            
    class VScale(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'
        
        @property
        def inputs(self):
            return {
                'vector': BType.VECTOR,
                'scale': BType.VALUE
            }

        @property
        def outputs(self):
            return {
                'vector': BType.VECTOR
            }
            
    class VNormalize(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'
        
        @property
        def inputs(self):
            return {
                'vector': BType.VECTOR
            }

        @property
        def outputs(self):
            return {
                'vector': BType.VECTOR
            }
            
    class VAbs(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'
        
        @property
        def inputs(self):
            return {
                'vector': BType.VECTOR
            }

        @property
        def outputs(self):
            return {
                'vector': BType.VECTOR
            }
            
    class VMin(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'
        
        @property
        def inputs(self):
            return {
                'vector1': BType.VECTOR,
                'vector2': BType.VECTOR
            }

        @property
        def outputs(self):
            return {
                'vector': BType.VECTOR
            }
            
    class VMax(NodeBase):
        @property
        def bnode(self):
            return 'ShaderNodeVectorMath'
        
        @property
        def inputs(self):
            return {
                'vector1': BType.VECTOR,
                'vector2': BType.VECTOR
            }

        @property
        def outputs(self):
            return {
                'vector': BType.VECTOR
            }