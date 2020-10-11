from vector import *
from material import *
from math import sqrt

class Object:
	def __init__(self):
		raise NotImplementedError

	def intersection(self, origin, direction):
		raise NotImplementedError

class Sphere(Object):
	def __init__(self, center, radius, material):
		self.center = center
		self.radius = radius
		self.material = material

	def intersection(self, origin, direction):
		s_dir = origin - self.center
		a = Vector.dot(direction, direction)
		b = Vector.dot(2*direction, s_dir)
		c = Vector.dot(s_dir, s_dir) - self.radius**2

		delta = b**2 - 4*a*c
		if delta < 0:
			return None

		t1 = (-b-sqrt(delta)) / (2*a)
		t2 = (-b+sqrt(delta)) / (2*a)

		t = min(t1, t2)
		if t <= 1:
			return None

		intersection_point = origin + t * direction
		surface_normal = ((1 / (intersection_point - self.center).norm) * (intersection_point - self.center)).unit_vector

		return t, intersection_point, surface_normal

class Box(Object):
	def __init__(self, box_min, box_max, material):
		self.b_min = box_min
		self.b_max = box_max
		self.material = material

	def intersection(self, origin, direction):
		t_min, t_max, ty_min, ty_max, tz_min, tz_max = 6 * [None]
		surface_normal = Vector(0, 0, 0)
		normal_y = Vector(0, 1, 0)
		normal_z = Vector(0, 0, 1)

		if direction.x >= 0:
			t_min = (self.b_min.x - origin.x) / direction.x
			t_max = (self.b_max.x - origin.x) / direction.x
			surface_normal = Vector(-1, 0, 0)
		else:
			t_min = (self.b_max.x - origin.x) / direction.x
			t_max = (self.b_min.x - origin.x) / direction.x
			surface_normal = Vector(1, 0, 0)

		if direction.y >= 0:
			ty_min = (self.b_min.y - origin.y) / direction.y
			ty_max = (self.b_max.y - origin.y) / direction.y
			normal_y = Vector(0, -1, 0)
		else:
			ty_min = (self.b_max.y - origin.y) / direction.y
			ty_max = (self.b_min.y - origin.y) / direction.y
			normal_y = Vector(0, 1, 0)

		if direction.z >= 0:
			tz_min = (self.b_min.z - origin.z) / direction.z
			tz_max = (self.b_max.z - origin.z) / direction.z
			normal_z = Vector(0, 0, -1)
		else:
			tz_min = (self.b_max.z - origin.z) / direction.z
			tz_max = (self.b_min.z - origin.z) / direction.z
			normal_z = Vector(0, 0, 1)

		if t_min > ty_max or ty_min > t_max:
			return None
		if ty_min > t_min:
			t_min = ty_min
			surface_normal = normal_y
		if ty_max < t_max:
			t_max = ty_max

		if t_min > tz_max or tz_min > t_max:
			return None
		if tz_min > t_min:
			t_min = tz_min
			surface_normal = normal_z
		if tz_max < t_max:
			t_max = tz_max

		if t_min <= 1:
			return None

		t = t_min

		intersection_point = origin + t * direction

		return t, intersection_point, surface_normal









