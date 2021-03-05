from . import NodeBase
from ..type_system import *


class AmbientOcclusion(NodeBase):
    @property
    def inputs(self):
        return {
            'samples': BType.VALUE,
            'inside': BType.BOOL,
            'only_local': BType.BOOL,
            'color': BType.COLOR,
            'distance': BType.VALUE,
            'normal': BType.VECTOR
        }
        
    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
            'ao': BType.VALUE
        }

class Attribute(NodeBase):
    @property
    def inputs(self):
        return {
            'type': BType.STRING,
            'name': BType.STRING
        }

    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
            'vector': BType.VECTOR,
            'fac': BType.VALUE,
            'alpha': BType.VALUE
        }

    @property
    def translation(self):
        return {
            'type': 'attribute_type',
            'name': 'attribute_name'
        }

class Bevel(NodeBase):
    @property
    def inputs(self):
        return {
            'samples': BType.VALUE,
            'radius': BType.VALUE,
            'normal': BType.VECTOR
        }
    
    @property
    def outputs(self):
        return {
            'vector': BType.VECTOR
        }

class CameraData(NodeBase):
    @property
    def inputs(self):
        return {}
    
    @property
    def outputs(self):
        return {
            'vector': BType.VECTOR,
            'zdepth': BType.VALUE,
            'distance': BType.VALUE
        }

class Fresnel(NodeBase):
    @property
    def inputs(self):
        return {
            'ior': BType.VALUE,
            'normal': BType.VECTOR
        }
    
    @property
    def outputs(self):
        return {
            'fac': BType.VALUE
        }
        
class Geometry(NodeBase):
    @property
    def inputs(self):
        return {}
    
    @property
    def outputs(self):
        return {
            'position': BType.VECTOR,
            'normal': BType.VECTOR,
            'tangent': BType.VECTOR,
            'true_normal': BType.VECTOR,
            'incoming': BType.VECTOR,
            'parametric': BType.VECTOR,
            'backfacing': BType.VALUE,
            'pointiness': BType.VALUE,
            'random_per_island': BType.VALUE
        }

class HairInfo(NodeBase):
    @property
    def inputs(self):
        return {}
    
    @property
    def outputs(self):
        return {
            'is_strand': BType.VALUE,
            'intercept': BType.VALUE,
            'thickness': BType.VALUE,
            'tangent_normal': BType.VECTOR,
            'random': BType.VALUE
        }

class LayerWeight(NodeBase):
    @property
    def inputs(self):
        return {
            'blend': BType.VALUE,
            'normal': BType.VECTOR
        }
    
    @property
    def outputs(self):
        return {
            'fresnel': BType.VALUE,
            'facing': BType.VALUE
        }

class LightPath(NodeBase):
    @property
    def inputs(self):
        return {}
    
    @property
    def outputs(self):
        return {
            'is_camera_ray': BType.VALUE,
            'is_shadow_ray': BType.VALUE,
            'is_diffuse_ray': BType.VALUE,
            'is_glossy_ray': BType.VALUE,
            'is_singular_ray': BType.VALUE,
            'is_reflection_ray': BType.VALUE,
            'is_transmission_ray': BType.VALUE,
            'ray_length': BType.VALUE,
            'ray_depth': BType.VALUE,
            'diffuse_depth': BType.VALUE,
            'glossy_depth': BType.VALUE,
            'transparent_depth': BType.VALUE,
            'transmission_depth': BType.VALUE
        }

class ObjectInfo(NodeBase):
    @property
    def inputs(self):
        return {}
    
    @property
    def outputs(self):
        return {
            'location': BType.VECTOR,
            'color': BType.COLOR,
            'object_index': BType.VALUE,
            'material_index': BType.VALUE,
            'random': BType.VALUE
        }

class ParticleInfo(NodeBase):
    @property
    def inputs(self):
        return {}
    
    @property
    def outputs(self):
        return {
            'index': BType.VALUE,
            'random': BType.VALUE,
            'age': BType.VALUE,
            'lifetime': BType.VALUE,
            'location': BType.VECTOR,
            'size': BType.VALUE,
            'velocity': BType.VECTOR,
            'angular_velocity': BType.VECTOR
        }

class RGB(NodeBase):
    @property
    def inputs(self):
        return {}
    
    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
        }

class Tangent(NodeBase):
    @property
    def inputs(self):
        return {
            'direction': BType.STRING,
            'axis': BType.STRING
        }
    
    @property
    def outputs(self):
        return {
            'tangent': BType.VECTOR
        }

    @property
    def translation(self):
        return {
            'direction': 'direction_type'
        }

class TextureCoordinate(NodeBase):
    @property
    def inputs(self):
        return {
            'from_instancer': BType.BOOL
        }
    
    @property
    def outputs(self):
        return {
            'generated': BType.VECTOR,
            'normal': BType.VECTOR,
            'uv': BType.VECTOR,
            'object': BType.VECTOR,
            'camera': BType.VECTOR,
            'window': BType.VECTOR,
            'reflection': BType.VECTOR
        }

class UVMap(NodeBase):
    @property
    def inputs(self):
        return {
            'from_instancer': BType.BOOL
        }
    
    @property
    def outputs(self):
        return {
            'uv': BType.VECTOR
        }

class VertexColor(NodeBase):
    @property
    def inputs(self):
        return {}
    
    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
            'alpha': BType.VALUE
        }

class VolumeInfo(NodeBase):
    @property
    def inputs(self):
        return {}
    
    @property
    def outputs(self):
        return {
            'color': BType.COLOR,
            'density': BType.VALUE,
            'flame': BType.VALUE,
            'temperature': BType.VALUE
        }

class Wireframe(NodeBase):
    @property
    def inputs(self):
        return {
            'pixel_size': BType.BOOL,
            'size': BType.VALUE
        }
    
    @property
    def outputs(self):
        return {
           'fac': BType.VALUE
        }

    @property
    def translation(self):
        return {
            'pixel_size': 'use_pixel_size'
        }