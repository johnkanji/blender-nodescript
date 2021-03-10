import bpy

from . import NodeBase
from ..type_system import *


class BrightContrast(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeBrightContrast'
    
    @property
    def inputs(self):
        return {
            'color': BType.COLOR,
            'bright': BType.VALUE,
            'contrast': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR
        }

class Gamma(NodeBase):
    @property
    def inputs(self):
        return {
            'color': BType.COLOR,
            'gamma': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR
        }

class HueSatVal(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeHueSaturation'
    
    @property
    def inputs(self):
        return {
            'hue': BType.VALUE,
            'sat': BType.VALUE,
            'value': BType.VALUE,
            'fac' : BType.VALUE,
            'color': BType.COLOR,
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR
        }

class Invert(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeInvert'
    
    @property
    def inputs(self):
        return {
            'fac': BType.VALUE,
            'color': BType.COLOR
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR
        }

class LightFalloff(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeLightFalloff'
    
    @property
    def inputs(self):
        return {
            'strength': BType.VALUE,
            'smooth': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'quadratic': BType.VALUE,
            'linear': BType.VALUE,
            'constant': BType.VALUE
        }

class RGBCurves(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeRGBCurve'
    
    @property
    def inputs(self):
        return {
            'fac': BType.VALUE,
            'color': BType.COLOR
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR
        }