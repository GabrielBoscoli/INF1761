from vector import *
from math import tan, pi

class Camera:
    # f - focal distance
    # fov - field of vision in degrees
    def __init__(self, w, h, fovy, f):
        self.w = w
        self.h = h
        self.fov = fovy
        self.f = f
        self.a = 2 * f * tan(pi * fovy / 360.)
        self.b = w * self.a / h
        
        self.xe = Vector(1, 0, 0)
        self.ye = Vector(0, 1, 0)
        self.ze = Vector(0, 0, 1)
    
    def position(self, eye, center, up):
        self.eye = eye
        self.ze = (center-eye).unit_vector
        self.xe = Vector.cross(self.ze, up).unit_vector
        self.ye = Vector.cross(self.ze, self.xe)

    def ray_origin(self):
        return self.eye

    def ray_direction(self, x, y):
        return self.f * self.ze + self.a * (y/self.h - 0.5) * self.ye + self.b * (x/self.w - 0.5) * self.xe
