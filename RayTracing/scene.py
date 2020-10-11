import matplotlib.pyplot as plt
import numpy as np
import itertools
from vector import *
from camera import *
from material import *
from objects import *
from light import *
from helper import *

class Scene:
	def __init__(self, camera, objects, light_sources):
		self.camera = camera
		self.objects = objects
		self.background_color = Vector(0.7, 0.7, 0.7)
		self.light_sources = light_sources
		self.recursion_limit = 1

	def find_intersection(self, origin, direction):
		min_t = np.inf
		intersection_point = None
		surface_normal = None
		intersection_obj = None
		for obj in self.objects:
			obj_data = obj.intersection(origin, direction)
			if obj_data == None:
				continue

			t, point, normal = obj_data
			if t < min_t:
				min_t = t
				intersection_point = point
				surface_normal = normal
				intersection_obj = obj

		return intersection_point, surface_normal, intersection_obj

	def ray_trace(self, origin, direction, recursion=0):
		color = self.background_color

		intersection_point, surface_normal, intersection_obj = self.find_intersection(origin, direction)

		if intersection_point != None:
			color = Vector(0, 0, 0)
			for light_source in self.light_sources:
				if not light_source.in_shadow(intersection_point, self.objects):
					color += light_source.compute_color(self.camera.eye, intersection_point, surface_normal, intersection_obj.material)
			color.clip_values()
		
		if intersection_obj != None and intersection_obj.material.mirror and recursion < self.recursion_limit:
			new_direction = (self.camera.eye - intersection_point).unit_vector.reflection(surface_normal)
			mirrom_dim_factor = 0.8
			color = self.ray_trace(intersection_point, new_direction, recursion+1) * mirrom_dim_factor

		return color

	def render(self):
		image = np.zeros((self.camera.w, self.camera.h, 3))
		origin = self.camera.ray_origin()
		for y, x in itertools.product(range(self.camera.w), range(self.camera.h)):
			direction = self.camera.ray_direction(x, y)
			image[y, x] = self.ray_trace(origin, direction).array
			progress_bar(y * self.camera.w + x, self.camera.w * self.camera.h)
		plt.figure(figsize=(5,5))
		plt.imshow(image)
		plt.show()

cam = Camera(1000, 1000, 90, 30)

eye = Vector(100, 40, 40)
center = Vector(0, 0, 0)
up = Vector(0, 1, 0)
cam.position(eye, center, up)

s_center = Vector(0, 20, 0)
s_radius = 25
s_diffuse = Vector(0, 0, 1)
s_specular = Vector(1, 1, 1)
s_material = Material(s_diffuse, s_specular)
sphere = Sphere(s_center, s_radius, s_material)

box_diffuse = Vector(0.7, 0.7, 0)
box_specular = Vector(1, 1, 1)
box_material = Material(box_diffuse, box_specular)
box_material2 = Material(box_diffuse, box_specular)

b1_min = Vector(-80, -50, -50)
b1_max = Vector(50, -45, 50)
box1 = Box(b1_min, b1_max, box_material)

b2_min = Vector(-80, -50, -60)
b2_max = Vector(50, 50, -50)
box2 = Box(b2_min, b2_max, box_material2)

light_position = Vector(60, 120, 40)
light_color = Vector(0.8, 0.8, 0.8)
light_source = PointLightSource(light_position, light_color)

light_position2 = Vector(0, 120, 120)
light_source2 = PointLightSource(light_position2, light_color)

ambient_light = AmbientLightSource(Vector(0.1, 0.1, 0.1))

scene = Scene(cam, [sphere, box1, box2], [light_source, light_source2, ambient_light])
scene.render()
