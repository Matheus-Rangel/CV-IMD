import numpy as np
import cv2
import matplotlib.pyplot as plt

def img_gradient(img):
    gradient = np.linspace(0,1, img.shape[0])
    img_b = np.transpose(img[:,:,0])
    img_b = np.multiply(img_b, gradient)
    img_g = np.transpose(img[:,:,1])
    img_g = np.multiply(img_g, gradient)
    img_r = np.transpose(img[:,:,2])
    img_r = np.multiply(img_r, gradient)
    img[:,:,0] = np.transpose(img_b)
    img[:,:,1] = np.transpose(img_g)
    img[:,:,2] = np.transpose(img_r)
    return img
if __name__ == "__main__":
    img = cv2.imread('img/messi.jpg')
    cv2.imwrite('img/messigradient.png',img_gradient(img))