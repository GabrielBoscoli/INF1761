import numpy as np

class Vector:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return "({}, {}, {})".format(self.x, self.y, self.z)

	@property
	def array(self):
		return np.array([self.x, self.y, self.z])

	def __add__(self, v):
		add_array = self.array + v.array
		add_vector = Vector(add_array[0], add_array[1], add_array[2])
		return add_vector

	def __iadd__(self, v):
		add_array = self.array + v.array
		add_vector = Vector(add_array[0], add_array[1], add_array[2])
		return add_vector

	def __sub__(self, v):
		sub_array = self.array - v.array
		sub_vector = Vector(sub_array[0], sub_array[1], sub_array[2])
		return sub_vector

	def __neg__(self):
		return Vector(-self.x, -self.y, -self.z)

	def __mul__(self, k):
		return Vector(k * self.x, k * self.y, k * self.z)

	def __rmul__(self, k):
		return Vector(k * self.x, k * self.y, k * self.z)

	@property
	def norm(self):
		return np.sqrt(np.sum(np.square(self.array)))

	def normalize(self):
		n = self.norm
		if n == 0:
			return
		self.x /= n
		self.y /= n
		self.z /= n

	def clip_values(self):
		self.x = max(self.x, 0)
		self.x = min(self.x, 1)
		self.y = max(self.y, 0)
		self.y = min(self.y, 1)
		self.z = max(self.z, 0)
		self.z = min(self.z, 1)

	def reflection(self, normal):
		return 2 * (Vector.dot(self, normal)/Vector.dot(self, self)) * normal - self

	@property
	def unit_vector(self):
		n = self.norm
		if n == 0:
			return Vector(0, 0, 0)
		unit = Vector(self.x/n, self.y/n, self.z/n)
		return unit

	@classmethod
	def dot(cls, u, v):
		return np.dot(u.array, v.array)

	@classmethod
	def cross(cls, u, v):
		cross_array = np.cross(u.array, v.array)
		cross_vector = Vector(cross_array[0], cross_array[1], cross_array[2])
		return cross_vector

	@classmethod
	def elementwise_product(cls, u, v):
		product_array = u.array * v.array
		product_vector = Vector(product_array[0], product_array[1], product_array[2])
		return product_vector
