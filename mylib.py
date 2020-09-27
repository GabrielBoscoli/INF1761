import numpy as np
import matplotlib.pyplot as plt

def show_gray(img, title):
    plt.figure(figsize=(8, 8))
    plt.title(title)
    plt.imshow(img, cmap="gray")
    plt.show()

def show_rgb(img,title):
    plt.figure(figsize=(8, 8))
    plt.title(title)
    plt.imshow(img)
    plt.show()

def show_hist(dat, title):
    plt.figure(figsize=(8, 8))
    plt.title(title)
    _ = plt.hist(dat, 255)
    plt.show()

def show_curve(x, y):
    plt.figure(figsize=(10, 4))
    plt.plot(x, y, color='b')
    plt.show()

def show_npy(arr):
    print(f'shape={arr.shape}, type={arr.dtype}')
    print(f'min= {np.amin(arr)}, max={np.amax(arr)}')