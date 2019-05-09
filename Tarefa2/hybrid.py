import numpy as np
import cv2

img = cv2.imread('messi.jpg', 0)
img2 = cv2.imread('soares.jpg', 0)
img_fft = np.fft.fft2(img)
img_fft = np.fft.fftshift(img_fft)
img2_fft = np.fft.fft2(img2)
img2_fft = np.fft.fftshift(img2_fft)

for u in range(img.shape[0]):
    for v in range(img.shape[1]):
        u1 = u - img.shape[0]/2
        v1 = v - img.shape[1]/2
        duv = np.sqrt(u1*u1 + v1*v1)
        if duv > 100:
            huv = 1
            huv2 = 0
        else:
            huv = 0
            huv2 = 1
        img_fft[u][v] = huv*img_fft[u][v]
        img2_fft[u][v] = huv2*img2_fft[u][v]

img_fft = np.fft.fftshift(img_fft)
img2_fft = np.fft.fftshift(img2_fft)

img = np.fft.ifft2(img_fft).astype(np.uint8)
img2 = np.fft.ifft2(img2_fft).astype(np.uint8)

cv2.imwrite('messi_soares.jpg', (img*0.5 + img2*0.5))