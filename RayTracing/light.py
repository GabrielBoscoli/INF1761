from vector import *
from objects import *

class LightSource:
	def __init__(self):
		raise NotImplementedError

	def in_shadow(self, point, objects):
		raise NotImplementedError

	def compute_color(self, eye, point, normal, material):
		raise NotImplementedError

class PointLightSource:
	def __init__(self, position, color):
		self.position = position
		self.color = color

	def in_shadow(self, point, objects):
		origin = point
		light_direction = (self.position - point).unit_vector
		for obj in objects:
			if obj.intersection(origin, light_direction) != None:
				return True
		return False

	def compute_color(self, eye, point, normal, material):
		light_direction = (self.position - point).unit_vector
		light_reflection = light_direction.reflection(normal)
		sight_direction = (eye - point).unit_vector
		n = material.specular_n
		diffuse_intensity = max(Vector.dot(light_direction, normal), 0)
		diffuse_color = Vector.elementwise_product(self.color, material.diffusion) * diffuse_intensity
		diffuse_color.clip_values()

		specular_intensity = max(Vector.dot(sight_direction, light_reflection), 0)
		specular_color = Vector.elementwise_product(self.color, material.specular) * (specular_intensity ** n)
		specular_color.clip_values()
		
		color = diffuse_color + specular_color
		color.clip_values()
		return color

class AmbientLightSource:
	def __init__(self, color):
		self.color = color

	def in_shadow(self, point, objects):
		return False

	def compute_color(self, eye, point, normal, material):
		color = Vector.elementwise_product(self.color, material.diffusion)
		color.clip_values()
		return color
