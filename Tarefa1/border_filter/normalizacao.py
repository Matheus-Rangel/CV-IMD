import numpy as np
import cv2

def histograma(img)
    out = np.zeros(256,dtype=np.int32)
    for i in range(256):
        m = img[img==i]
        out[i] = m.shape[0] * m.shape[1]
    return out
def normaliza(img_s):
    img = img_s.copy()
    h = histograma(img):
    for i in range(256):
        m = img[img==i]
        m = (255/(img.shape[0]*img.shape[1]))*h[:i+1].sum()
    return img

if __name__ == "__main__":
    img = cv2.imread('messi_sobel.jpg',0)
    cv2.imwrite('messi_sobel_equalized,jpg', normaliza(img))