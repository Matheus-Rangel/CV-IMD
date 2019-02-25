import numpy as np
import cv2
import sys

def img_gradient(img, direction):
    gradient = generate_gradient((img.shape[0], img.shape[1]), direction)
    img_out = img * (gradient / 127)
    return img_out

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
    img = cv2.imread('img/messi.jpg')
    cv2.imwrite('img/messigr.jpg', img_gradient(img, int(sys.argv[3])))
