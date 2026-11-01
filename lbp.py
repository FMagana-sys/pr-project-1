import numpy as np

def lbp_pixel(image, i, j):

    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    N = 0
   
    for k, (di, dj) in enumerate(neighbors):
    
        if image[i + di][j + dj] >= image[i][j]:
    
            N = N + 2**k
    
    return N

def _check_size(image):

    if image.shape[0] < 3 or image.shape[1] < 3:
        raise ValueError("The image must be of at least 3x3")


def lbp_image(image):

    _check_size(image)
    
    T = np.zeros_like(image, dtype = np.uint8)

    # Ciclo para recorrer las filas
    for i in range(1, len(image) - 1):

        # Ciclo para recorrer las columnas
        for j in range(1, len(image[0]) - 1):
            
            T[i, j] = lbp_pixel(image, i, j)
    return T

def lbp_histogram(lbp_map):

    _check_size(lbp_map)
    
    interior = lbp_map[1:-1, 1:-1]

    bcount = np.bincount(interior.ravel(), minlength = 256)
    bcount = bcount / (np.size(interior))
    return bcount