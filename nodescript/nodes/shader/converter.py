from .. import NodeBase
from ...type_system import *


class Blackbody(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeBlackbody'
    
    @property
    def inputs(self):
        return {
            'temperature': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR
        }
    
class Clamp(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeClamp'
    
    @property
    def inputs(self):
        return {
            'type': BType.STRING,
            'value': BType.VALUE,
            'min': BType.VALUE,
            'max': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'result': BType.VALUE
        }

    @property
    def translation(self):
        return {
            'type': 'clamp_type'
        }

class ColorRamp(NodeBase):
    @property
    def bnode(self):
        raise NotImplementedError
    
    @property
    def inputs(self):
        return {
            'fac': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
            'alpha': BType.VALUE
        }

class CombineHSV(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeCombineHSV'
    
    @property
    def inputs(self):
        return {
            'h': BType.VALUE,
            's': BType.VALUE,
            'v': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR
        }

class CombineRGB(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeCombineRGB'
    
    @property
    def inputs(self):
        return {
            'r': BType.VALUE,
            'g': BType.VALUE,
            'b': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR
        }

class CombineXYZ(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeCombineXYZ'
    
    @property
    def inputs(self):
        return {
            'x': BType.VALUE,
            'y': BType.VALUE,
            'z': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'vector': BType.VECTOR
        }

class MapRange(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeMapRange'
    
    @property
    def inputs(self):
        return {
            'value': BType.VALUE,
            'type': BType.STRING,
            'clamp': BType.BOOL,
            'from_min': BType.VALUE,
            'from_max': BType.VALUE,
            'to_min': BType.VALUE,
            'to_max': BType.VALUE,
            'steps': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'result': BType.VALUE
        }

    @property
    def translation(self):
        return {
            'type': 'interpolation_type'
        }

class RGBToBW(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeRGBToBW'
    
    @property
    def inputs(self):
        return {
            'color': BType.COLOR
        }

    @property
    def outputs(self):
        return {
            'value': BType.VALUE
        }

class SeparateHSV(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeSeparateHSV'
    
    @property
    def inputs(self):
        return {
            'color': BType.COLOR
        }

    @property
    def outputs(self):
        return {
            'h': BType.VALUE,
            's': BType.VALUE,
            'v': BType.VALUE
        }

class SeparateRGB(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeSeparateRGB'
    
    @property
    def inputs(self):
        return {
            'color': BType.COLOR
        }

    @property
    def outputs(self):
        return {
            'r': BType.VALUE,
            'g': BType.VALUE,
            'b': BType.VALUE
        }

class SeparateXYZ(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeSeparateXYZ'
    
    @property
    def inputs(self):
        return {
            'vector': BType.VECTOR
        }

    @property
    def outputs(self):
        return {
            'x': BType.VALUE,
            'y': BType.VALUE,
            'z': BType.VALUE
        }

class ShaderToRGB(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeShaderToRGB'

    @property
    def inputs(self):
        return {
            'shader': BType.SHADER
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
            'alpha': BType.VALUE
        }

class Wavelength(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeWavelength'
    
    @property
    def inputs(self):
        return {
            'wavelength': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR
        }