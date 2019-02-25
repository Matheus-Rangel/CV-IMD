import numpy as np
import cv2

def img_red(img):
    img_out = np.array(img)
    img_out[:,:,0] = 0
    img_out[:,:,1] = 0
    return img_out

def img_green(img):
    img_out = np.array(img)
    img_out[:,:,0] = 0
    img_out[:,:,2] = 0
    return img_out

def img_blue(img):
    img_out = np.array(img)
    img_out[:,:,1] = 0
    img_out[:,:,2] = 0
    return img_out

if __name__ == "__main__":
    img_bgr = cv2.imread('img/messi.jpg', )
    cv2.imwrite('img/messired.jpg',img_red(img_bgr))
    cv2.imwrite('img/messigreen.jpg',img_green(img_bgr))
    cv2.imwrite('img/messiblue.jpg',img_blue(img_bgr))