from filters import *
import cv2
import os

path = 'segundoConjunto'
path_dest = 'resultados'
if __name__ == "__main__":
    img_name = 'ruidoSalPimenta.jpg'
    img = cv2.imread(os.path.join(path, img_name),0)
    directory = os.path.join(path_dest, img_name.split('.')[0])
    if not os.path.exists(directory):
        os.makedirs(directory)
    cv2.imwrite(os.path.join(directory, 'arithmetic_mean.jpg'), arithmetic_mean(img, 1))
    cv2.imwrite(os.path.join(directory,'geometric_mean.jpg'), geometric_mean(img, 1))
    cv2.imwrite(os.path.join(directory, 'alpha_mean.jpg'), alpha_mean(img, 1, 2))
    cv2.imwrite(os.path.join(directory, 'dot_mean.jpg'), dot_mean(img, 1))
    cv2.imwrite(os.path.join(directory, 'harmonic_mean.jpg'), harmonic_mean(img, 1))
    cv2.imwrite(os.path.join(directory, 'median.jpg'), median(img, 1))
    cv2.imwrite(os.path.join(directory, 'min.jpg'), min(img, 1))
    cv2.imwrite(os.path.join(directory, 'max.jpg'), max(img, 1))
