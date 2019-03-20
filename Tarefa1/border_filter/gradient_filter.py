import numpy as np
import cv2
kernels = [np.ones(((i+1)*2 + 1, (i+1)*2 + 1)) for i in range(7)]
def gradient_filter(gradient, img):
    gradient = gradient - gradient.min()
    interval = gradient.max()/6
    img_out = img.copy()
    img_out[0:6, :] = 0
    img_out[:,0:6] = 0
    img_out[img_out.shape[0]-5:img_out.shape[0], :] = 0
    img_out[:, img_out.shape[1]-5:img_out.shape[1]] = 0
    i = 7
    while i < img_out.shape[0] - 6:
        j = 7
        while j < img_out.shape[1] - 6:
            kernel = kernels[0]
            if gradient[i,j] < interval:
                kernel = kernels[5]
            elif gradient[i,j] < interval*2:
                kernel = kernels[4]
            elif gradient[i,j] < interval*3:
                kernel = kernels[3]
            elif gradient[i,j] < interval*4:
                kernel = kernels[2]
            elif gradient[i,j] < interval*5:
                kernel = kernels[1]
            rad = int((kernel.shape[0] - 1)/2)
            img_out[i,j] = (img[i-rad:i+rad+1,j-rad:j+rad+1] * kernel).sum()/kernel.sum()
            j += 1
        i += 1
    return img_out
if __name__ == "__main__":
    gradient = cv2.imread('messi_sobel.jpg', 0)
    img = cv2.imread('messi.jpg', 0)
    cv2.imwrite('messi_filter.jpg', gradient_filter(gradient, img))