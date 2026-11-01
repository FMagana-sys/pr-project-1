from skimage import data
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter


def lbp_pixel(image, i, j):

    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    N = 0
   
    for k, (di, dj) in enumerate(neighbors):
    
        if image[i + di][j + dj] >= image[i][j]:
    
            N = N + 2**k
    
    return N

def lbp_image(image):

    T = np.zeros_like(image, dtype = np.uint8)

    # Ciclo para recorrer las filas
    for i in range(1, len(image) - 1):

        # Ciclo para recorrer las columnas
        for j in range(1, len(image[0]) - 1):
            
            T[i, j] = lbp_pixel(image, i, j)
    return T

# ----------------------------------------------------------------

camera = data.camera() # Takes an example image from a database

inicio = perf_counter() # Time counter initiation

mapa = lbp_image(camera) # LBP values Map

fin = perf_counter() # Time counter end


fig, ejes = plt.subplots(1,2) # Plotting a row of 2 figures
ejes[0].imshow(camera, cmap = 'gray') # First Figure
ejes[1].imshow(mapa, cmap = 'gray') # Second Figure

plt.show() # Show figures