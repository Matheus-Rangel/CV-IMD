import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import os

def denoise1(imgs):
    img = cv2.fastNlMeansDenoisingMulti(imgs, 8, 1)
    return img

def denoise2(imgs):
    img_out = imgs[0] * 0
    img_out = img_out.astype('int')
    for img in imgs:
        img_out += img
    img_out = np.floor_divide(img_out, len(imgs)) 
    return img_out

def colormap():
    cdict = {'red': ((0.0, 0.0, 0.0),
                    (1.0, 0.7, 0.7)),

         'green':   ((0.0, 0.0, 0.0),
                    (0.5, 0.0, 0.0),
                    (1.0, 0.6, 0.6)),

         'blue':  ((0.0, 0.0, 0.0),
                   (1.0, 1.0, 1.0))
        }
    return LinearSegmentedColormap('custom_cmap', cdict)
if __name__ == "__main__":
    imgs = []
    for img in os.listdir('img'):
        imgs.append(cv2.imread('img/' + img, 0))
    cv2.imwrite('denoise/denoise1.jpg', denoise1(imgs))
    cv2.imwrite('denoise/denoise2.jpg', denoise2(imgs))
    plt.imsave('denoise/denoise_colored.jpg', denoise2(imgs)*5, cmap='plasma')