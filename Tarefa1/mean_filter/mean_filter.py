import numpy as np
import cv2

def black_bars(img, black_width, space_width):
    img_out = img.copy()
    img_out[img_out<135] = img_out[img_out<135] + 120
    img_out[img_out>=135] = 255
    i = 0
    while i < img_out.shape[1]:
        img_out[:,i:i+black_width] = 0
        i = i + black_width + space_width
    return img_out

def mean_filter(img, kernel_rad):
    img_out = img.copy()
    kernel = np.ones((kernel_rad*2 + 1, kernel_rad*2 + 1), int)
    i = kernel_rad
    j = kernel_rad
    while i < img.shape[0] - kernel_rad:
        j = kernel_rad
        while j < img.shape[1] - kernel_rad:
            neighbors = img_out[i - kernel_rad:i + kernel_rad + 1,j - kernel_rad:j + kernel_rad + 1]
            img_out[i,j] = ((neighbors * kernel).sum())/(kernel.sum())
            j = j + 1
        i = i + 1
    return img_out

if __name__ == "__main__":
    img = cv2.imread('messi.jpg',0)
    cv2.imwrite('messi_mean_filter.jpg', mean_filter(img, 5))
    img = black_bars(img, 40, 15)
    cv2.imwrite('messi_bars.jpg', img)
    img = mean_filter(img, 20)
    cv2.imwrite('messi_filter.jpg', img)