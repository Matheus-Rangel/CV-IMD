import numpy as np
import cv2
def border_sobel(img):
    img_sobel_x = np.array(img,np.int32)
    img_sobel_y = np.array(img,np.int32)
    sobel_x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    sobel_y = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    i = 1
    while i < img.shape[0] - 1:
        j = 1
        while j < img.shape[1] - 1:
            img_sobel_x[i,j] = (img[i-1:i+2,j-1:j+2] * sobel_x).sum()
            img_sobel_y[i,j] = (img[i-1:i+2,j-1:j+2] * sobel_y).sum()
            j += 1
        i += 1
    img_sobel_x_square = np.square(img_sobel_x)
    img_sobel_y_square = np.square(img_sobel_y)
    gradient = np.sqrt(img_sobel_y_square + img_sobel_x_square)
    gradient = 255*(gradient + 1020)/2040
    return gradient

def border_prewitt(img):
    img_prewitt_x = np.array(img,np.int32)
    img_prewitt_y = np.array(img,np.int32)
    prewitt_x = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    prewitt_y = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
    i = 1
    while i < img.shape[0] - 1:
        j = 1
        while j < img.shape[1] - 1:
            img_prewitt_x[i,j] = (img[i-1:i+2,j-1:j+2] * prewitt_x).sum()
            img_prewitt_y[i,j] = (img[i-1:i+2,j-1:j+2] * prewitt_y).sum()
            j += 1
        i += 1
    img_prewitt_x_square = np.square(img_prewitt_x)
    img_prewitt_y_square = np.square(img_prewitt_y)
    gradient = np.sqrt(img_prewitt_y_square + img_prewitt_x_square)
    gradient = 255*(gradient + 1020)/2040
    return gradient

def border_filter(gradient, delimiter):
    border = gradient.copy()
    border[border<delimiter]=0
    border[border>=delimiter]=255
    return border

if __name__ == "__main__":
    img = cv2.imread('/home/matheus/projects/CV-IMD/Tarefa1/mean_filter/messi.jpg',0)
    sobel = border_sobel(img)
    prewitt = border_prewitt(img)
    sobel_border = border_filter(sobel, 180)
    prewitt_border = border_filter(prewitt, 180)
    cv2.imwrite('messi_sobel.jpg', sobel)
    cv2.imwrite('messi_prewitt.jpg', prewitt)
    cv2.imwrite('messi_sobel_border.jpg', sobel_border)
    cv2.imwrite('messi_prewitt_border.jpg', prewitt_border)