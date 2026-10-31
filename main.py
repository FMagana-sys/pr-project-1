from skimage import data
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter

camera = data.camera()
# top_left = camera[:50, :50]
# plt.imshow(top_left, cmap = 'gray')
# plt.show()


filas, columnas = camera.shape
# (512, 512)
# Son (filas, columnas)

print(f'El valor minimo de camera es: {camera.min()}, y el valor maximo es: {camera.max()}')