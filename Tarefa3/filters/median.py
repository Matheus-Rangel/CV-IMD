import numpy as np
def median(img_in, kernel_rad):
    img = img_in.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x1 = i - kernel_rad   
            x1 = 0 if x1 < 0 else x1
            
            x2 = i + 1 + kernel_rad
            x2 = img.shape[0] if x2>img.shape[0] else x2
            
            y1 = j - kernel_rad
            y1 = 0 if y1 < 0 else y1
            
            y2 = j + 1 + kernel_rad
            y2 = img.shape[1] if y2>img.shape[1] else y2 
            
            neighbors = img_in[x1:x2,y1:y2] 
            neightbors = np.reshape(neighbors, neighbors.shape[0] * neighbors.shape[1])
            img[i][j] = np.median(neighbors)
    return img