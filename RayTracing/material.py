class Material:
	def __init__(self, diffusion, specular, specular_n=50, mirror=False):
		self.diffusion = diffusion
		self.specular = specular
		self.specular_n = specular_n
		self.mirror = mirror