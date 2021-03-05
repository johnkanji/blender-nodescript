from . import NodeBase
from ..type_system import *


class Add(NodeBase):
    @property
    def inputs(self):
        return {
            'shader1': BType.SHADER,
            'shader2': BType.SHADER
        }

    @property
    def outputs(self):
        return {
            'shader': BType.SHADER
        }

class Diffuse(NodeBase):
    @property
    def inputs(self):
        return {
            'color': BType.COLOR,
            'roughness': BType.VALUE,
            'normal': BType.VECTOR
        }

    @property
    def outputs(self):
        return {
            'shader': BType.SHADER
        }

class Emission(NodeBase):
    @property
    def inputs(self):
        return {
            'color': BType.COLOR,
            'strength': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'shader': BType.SHADER
        }

class Glass(NodeBase):
    @property
    def inputs(self):
        return {
            'distribution': BType.STRING,
            'color': BType.COLOR,
            'roughness': BType.VALUE,
            'ior': BType.VALUE,
            'normal': BType.VECTOR
        }

    @property
    def outputs(self):
        return {
            'shader': BType.SHADER
        }

class Holdout(NodeBase):
    @property
    def inputs(self):
        return {}

    @property
    def outputs(self):
        return {
            'shader': BType.SHADER
        }

class Mix(NodeBase):
    @property
    def inputs(self):
        return {
            'fac': BType.VALUE,
            'shader1': BType.SHADER,
            'shader2': BType.SHADER
        }

    @property
    def outputs(self):
        return {
            'shader': BType.SHADER
        }

class Principled(NodeBase):
    @property
    def inputs(self):
        return {
            'distribution': BType.STRING,
            'subsurface_method': BType.STRING,
            'base_color': BType.COLOR,
            'subsurface': BType.VALUE,
            'subsurface_radius': BType.VECTOR,
            'subsurface_color': BType.COLOR,
            'metallic': BType.VALUE,
            'specular': BType.VALUE,
            'specular_tint': BType.VALUE,
            'roughness': BType.VALUE,
            'anisotropic': BType.VALUE,
            'anisotropic_rotation': BType.VALUE,
            'sheen': BType.VALUE,
            'sheen_tint': BType.VALUE,
            'clearcoat': BType.VALUE,
            'clearcoat_roughness': BType.VALUE,
            'ior': BType.VALUE,
            'transmission': BType.VALUE,
            'transmission_roughness': BType.VALUE,
            'emission': BType.COLOR,
            'emission_strength': BType.VALUE,
            'alpha': BType.VALUE,
            'normal': BType.VECTOR,
            'clearcoat_normal': BType.VECTOR,
            'tangent': BType.VECTOR
        }

    @property
    def outputs(self):
        return {
            'shader': BType.SHADER
        }

class Refraction(NodeBase):
    @property
    def inputs(self):
        return {
            'distribution': BType.STRING,
            'color': BType.COLOR,
            'roughness': BType.VALUE,
            'ior': BType.VALUE,
            'normal': BType.VECTOR
        }

    @property
    def outputs(self):
        return {
            'shader': BType.SHADER
        }

class Specular(NodeBase):
    @property
    def inputs(self):
        return {
            'base_color': BType.COLOR,
            'specular': BType.COLOR,
            'roughness': BType.VALUE,
            'emissive_color': BType.COLOR,
            'transparency': BType.VALUE,
            'normal': BType.VECTOR,
            'clearcoat': BType.VALUE,
            'clearcoat_roughness': BType.VALUE,
            'clearcoat_normal': BType.VECTOR,
            'ambient_occlusion': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'shader': BType.SHADER
        }

class SubsurfaceScattering(NodeBase):
    @property
    def inputs(self):
        return {
            'falloff': BType.STRING,
            'color': BType.COLOR,
            'scale': BType.VALUE,
            'radius': BType.VECTOR,
            'texture_blur': BType.VALUE,
            'normal': BType.VECTOR
        }

    @property
    def outputs(self):
        return {
            'shader': BType.SHADER
        }

class Translucent(NodeBase):
    @property
    def inputs(self):
        return {
            'color': BType.COLOR,
            'normal': BType.VECTOR
        }

    @property
    def outputs(self):
        return {
            'shader': BType.SHADER
        }

class Transparent(NodeBase):
    @property
    def inputs(self):
        return {
            'color': BType.COLOR
        }

    @property
    def outputs(self):
        return {
            'shader': BType.SHADER
        }

class VolumeAbsorption(NodeBase):
    @property
    def inputs(self):
        return {
            'color': BType.COLOR,
            'density': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'shader': BType.SHADER
        }

class VolumeScatter(NodeBase):
    @property
    def inputs(self):
        return {
            'color': BType.COLOR,
            'density': BType.VALUE,
            'anisotropy': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'shader': BType.SHADER
        }