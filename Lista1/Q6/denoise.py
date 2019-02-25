import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
def denoise1(imgs):
    img = cv2.fastNlMeansDenoisingMulti(imgs, 8, 1)
    return img

def denoise2(imgs):
    img_out = imgs[0] * 0
    for img in imgs:
        img_out += img
    return img_out
def colormap():
    cdict = {'red':((0.0, 0.0, 0.0),
                   (0.5, 0.0, 1.0),
                   (1.0, 0.1, 1.0)),

         'green': ((0.0, 0.0, 0.0),
                   (1.0, 0.0, 0.0)),

         'blue':  ((0.0, 0.0, 0.1),
                   (0.5, 1.0, 0.0),
                   (1.0, 0.0, 0.0))
        }
    return LinearSegmentedColormap('custom_cmap', cdict)
if __name__ == "__main__":
    imgs = []
    for img in os.listdir('img'):
        imgs.append(cv2.imread('img/' + img, 0))
    cv2.imwrite('denoise/denoise1.jpg', denoise1(imgs))
    cv2.imwrite('denoise/denoise2.jpg', denoise2(imgs))
    plt.imsave('denoise/denoise_colored.jpg', denoise1(imgs), cmap='hot')