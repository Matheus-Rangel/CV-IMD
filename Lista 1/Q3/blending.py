import numpy as np
import cv2
import matplotlib.pyplot as plt

def img_blending(img1, img2):
    img_out = (img1 * 0.5) + (img2 * 0.5)
    return img_out

if __name__ == "__main__":
    img1 = cv2.imread('img/messi.jpg')
    img2 = cv2.imread('img/messiinverted.jpg')
    cv2.imwrite('img/messibleding.png',img_blending(img1, img2))