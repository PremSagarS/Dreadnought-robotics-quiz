import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('input.jpeg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
edges = cv.Canny(img,100,200)
plt.imshow(edges,cmap = 'gray')
plt.savefig("output.jpeg")