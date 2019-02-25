import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
def denoise(imgs):
    img = cv2.fastNlMeansDenoisingMulti(imgs, 8, 1)
    return img

if __name__ == "__main__":
    imgs = []
    for img in os.listdir('img'):
        imgs.append(cv2.imread('img/' + img, 0))
    cv2.imwrite('img/denoise.jpg', denoise(imgs))