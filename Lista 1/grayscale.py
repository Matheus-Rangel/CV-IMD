import numpy as numpy
import cv2
import matplotlib.pyplot as plt

img_rgb = cv2.imread('messi.jpg', 1)
img_original = cv2.imread('messi.jpg', -1)
img_grayscale = cv2.imread('messi.jpg', 0)