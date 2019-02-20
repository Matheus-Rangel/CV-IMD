import numpy as np
import cv2
import matplotlib.pyplot as plt

def img_inversition(img):
    img_out = img[:, ::-1]
    return img_out

if __name__ == "__main__":
    img_bgr = cv2.imread('img/messi.jpg', )
    cv2.imwrite('img/messiinverted.jpg',img_inversition(img_bgr))