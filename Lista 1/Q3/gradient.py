import numpy as np
import cv2
import sys

def img_gradient(img):
    gradient = np.linspace(0.5, 1, img.shape[0])
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

def generate_gradient(resolution, direction):
    """
    Paramentros
    resolution: resolution of the gradient
    direction: 1 for up down, 2 for right left, 3 for down up, 4 for left right
    """
    x = resolution[0]
    y = resolution[1]
    img = np.ones((x,y,3), dtype=int) * 255
    if direction == 1:
        gradient = np.linspace(0, 1, x)
        img = np.transpose(img, axes=(1,0,2))
        img[:,:,0] = img[:,:,0] * gradient
        img[:,:,1] = img[:,:,1] * gradient
        img[:,:,2] = img[:,:,2] * gradient
        img = np.transpose(img, axes=(1,0,2))
    elif direction == 2:
        gradient = np.linspace(0, 1, y)
        img[:,:,0] = img[:,:,0] * gradient
        img[:,:,1] = img[:,:,1] * gradient
        img[:,:,2] = img[:,:,2] * gradient
    elif direction == 3:
        gradient = np.linspace(1, 0, x)
        img = np.transpose(img, axes=(1,0,2))
        img[:,:,0] = img[:,:,0] * gradient
        img[:,:,1] = img[:,:,1] * gradient
        img[:,:,2] = img[:,:,2] * gradient
        img = np.transpose(img, axes=(1,0,2))
    elif direction == 4:
        gradient = np.linspace(1, 0, y)
        img[:,:,0] = img[:,:,0] * gradient
        img[:,:,1] = img[:,:,1] * gradient
        img[:,:,2] = img[:,:,2] * gradient
    else:
        raise ValueError("Direction must have values 1,2,3 or 4")   
    return img

if __name__ == "__main__":
    cv2.imwrite('img/gradient.jpg',generate_gradient((int(sys.argv[1]), int(sys.argv[2])), int(sys.argv[3])))
    print('gradient.jpg criado')