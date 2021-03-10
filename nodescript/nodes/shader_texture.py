from . import NodeBase
from ..type_system import *


class Brick(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeTexBrick'
    
    @property
    def inputs(self):
        return {
            'offset': BType.VALUE,
            'offset_frequency': BType.VALUE,
            'squash': BType.VALUE,
            'squash_frequency': BType.VALUE,
            'vector': BType.VECTOR,
            'color1': BType.COLOR,
            'color2': BType.COLOR,
            'mortar': BType.COLOR,
            'scale': BType.VALUE,
            'mortar_size': BType.VALUE,
            'mortar_smooth': BType.VALUE,
            'bias': BType.VALUE,
            'brick_width': BType.VALUE,
            'row_height': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
            'fac': BType.VALUE
        }

class Checker(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeTexChecker'

    @property
    def inputs(self):
        return {
            'vector': BType.VECTOR,
            'color1': BType.COLOR,
            'color2': BType.COLOR,
            'scale': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
            'fac': BType.VALUE
        }

class Environment(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeTexEnvironment'
    
    @property
    def inputs(self):
        return {
            'interpolation': BType.STRING,
            'projection': BType.STRING,
            'vector': BType.VECTOR
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR
        }

class Gradient(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeTexGradient'
    
    @property
    def inputs(self):
        return {
            'type': BType.STRING,
            'vector': BType.VECTOR
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
            'fac': BType.VALUE
        }

    @property
    def translation(self):
        return {
            'type': 'gradient_type'
        }

class IES(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeTexIES'
    
    @property
    def inputs(self):
        return {
            'vector': BType.VECTOR,
            'strength': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'fac': BType.VALUE
        }

class Image(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeTexImage'

    @property
    def inputs(self):
        return {
            'interpolation': BType.STRING,
            'projection': BType.STRING,
            'extension': BType.STRING,
            'vector': BType.VECTOR
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
            'alpha': BType.VALUE
        }

class Magic(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeTexMagic'
    
    @property
    def inputs(self):
        return {
            'depth': BType.VALUE,
            'vector': BType.VECTOR,
            'scale': BType.VALUE,
            'distortion': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
            'fac': BType.VALUE
        }

    @property
    def translation(self):
        return {
            'depth': 'turbulence_depth'
        }

class Musgrave(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeTexMusgrave'
    
    @property
    def inputs(self):
        return {
            'dimensions': BType.STRING,
            'type': BType.STRING,
            'vector': BType.VECTOR,
            'w': BType.VALUE,
            'scale': BType.VALUE,
            'detail': BType.VALUE,
            'dimension': BType.VALUE,
            'lacunarity': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'height': BType.VALUE
        }

    @property
    def translation(self):
        return {
            'dimensions': 'musgrave_dimensions',
            'type': 'musgrave_type'
        }

class Noise(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeTexNoise'

    @property
    def inputs(self):
        return {
            'dimensions': BType.STRING,
            'vector': BType.VECTOR,
            'w': BType.VALUE,
            'scale': BType.VALUE,
            'detail': BType.VALUE,
            'roughness': BType.VALUE,
            'distortion': BType.VALUE,
        }

    @property
    def outputs(self):
        return {
            'fac': BType.VALUE,
            'color': BType.COLOR
        }

    @property
    def translation(self):
        return {
            'dimensions': 'noise_dimensions'
        }

class PointDensity(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeTexPointDensity'
    
    @property
    def inputs(self):
        return {
            'point_source': BType.STRING,
            'space': BType.STRING,
            'radius': BType.VALUE,
            'interpolation': BType.STRING,
            'resolution': BType.VALUE,
            'color_source': BType.STRING,
            'vector': BType.VECTOR
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
            'density': BType.VALUE
        }

class Sky(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeTexSky'
    
    @property
    def inputs(self):
        return {
            'sun_disc': BType.BOOL,
            'sun_size': BType.VALUE,
            'sun_intensity': BType.VALUE,
            'sun_elevation': BType.VALUE,
            'sun_rotation': BType.VALUE,
            'altitude': BType.VALUE,
            'air': BType.VALUE,
            'dust': BType.VALUE,
            'ozone': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
        }

class Voronoi(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeTexVoronoi'

    @property
    def inputs(self):
        return {
            'dimensions': BType.STRING,
            'feature': BType.STRING,
            'distance': BType.STRING,
            'vector': BType.VECTOR,
            'w': BType.VALUE,
            'scale': BType.VALUE,
            'smoothness': BType.VALUE,
            'exponent': BType.VALUE,
            'randomness': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'distance': BType.VALUE,
            'color': BType.COLOR,
            'position': BType.VECTOR,
            'w': BType.VALUE
        }

    @property
    def translation(self):
        return {
            'dimensions': 'voronoi_dimensions',
        }

class Wave(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeTexWave'
    
    @property
    def inputs(self):
        return {
            'type': BType.STRING,
            'direction': BType.STRING,
            'profile': BType.STRING,
            'vector': BType.VECTOR,
            'scale': BType.VALUE,
            'distortion': BType.VALUE,
            'detail': BType.VALUE,
            'detail_scale': BType.VALUE,
            'detail_roughness': BType.VALUE,
            'phase_offset': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
            'fac': BType.VALUE
        }

    @property
    def translation(self):
        return {
            'type': 'wave_type',
            'profile': 'wave_profile'
        }

class WhiteNoise(NodeBase):
    @property
    def bnode(self):
        return 'ShaderNodeTexWhiteNoise'

    @property
    def inputs(self):
        return {
            'vector': BType.VECTOR,
            'w': BType.VALUE
        }

    @property
    def outputs(self):
        return {
            'fac': BType.VALUE,
            'color': BType.COLOR
        }

    @property
    def translation(self):
        return {
            'dimensions': 'noise_dimensions'
        }
