from skimage import data
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter

import lbp # LBP functions



camera = data.camera() # Takes an example image from a database

mapa = lbp.lbp_image(camera) # LBP values Map



# fig, ejes = plt.subplots(1,2) # Plotting a row of 2 figures
# ejes[0].imshow(camera, cmap = 'gray') # First Figure
# ejes[1].imshow(mapa, cmap = 'gray') # Second Figure

# plt.show() # Show figures

# -----------------Milestone 2---------------------------

h = lbp.lbp_histogram(mapa) 


    

