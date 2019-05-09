import cv2
import numpy as np
from matplotlib import pyplot as plt

original = cv2.imread('primeiroConjunto/cristo.jpg',0)
ruido = cv2.imread('primeiroConjunto/ruido6.jpg',0)
hist_original = cv2.calcHist([original],[0],None,[256],[0,256])
hist_ruido = cv2.calcHist([ruido],[0],None,[256],[0,256])
plt.plot(hist_ruido)
plt.xlim([0,256])

plt.show()
