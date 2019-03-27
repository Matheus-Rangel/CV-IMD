from filters import *
import cv2
import os

path = 'segundoConjunto'
path_dest = 'resultados'
if __name__ == "__main__":
    img_name = 'ruidoGaussiano.jpg'
    img = cv2.imread(os.path.join(path, img_name))
    cv2.imwrite(os.path.join(path_dest + img_name.split('.')[0] + '/arithmetic_mean.jpg', arithmetic_mean(img, 1))
    cv2.imwrite(path_dest + img_name.split('.')[0] + '/geometric_mean.jpg', geometric_mean(img, 1))
    cv2.imwrite(path_dest + img_name.split('.')[0] + '/alpha_mean.jpg', alpha_mean(img, 1, 2))
    cv2.imwrite(path_dest + img_name.split('.')[0] + '/dot_mean.jpg', dot_mean(img, 1))
    cv2.imwrite(path_dest + img_name.split('.')[0] + '/harmonic_mean.jpg', harmonic_mean(img, 1))
    cv2.imwrite(path_dest + img_name.split('.')[0] + '/median.jpg', median(img, 1))
    cv2.imwrite(path_dest + img_name.split('.')[0] + '/min.jpg', min(img, 1))
    cv2.imwrite(path_dest + img_name.split('.')[0] + '/max.jpg', max(img, 1))
