import numpy as np

def novo(x,y,z):
    return np.array([x,y,z])
  
def norma(v):
    return np.sqrt(np.sum(np.square(v)))


def unitario(v):
    s = norma(v)
    return v/s

def vetorial(u,v):
    return np.array([u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0]])
    