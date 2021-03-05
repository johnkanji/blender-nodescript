from . import NodeBase
from ..type_system import *


class BrightContrast(NodeBase):
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