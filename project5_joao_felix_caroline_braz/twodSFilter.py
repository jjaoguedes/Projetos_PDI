from math import floor
import numpy as np
from imagePad4e import imagePad4e

def twodSFilter(f , w):

    #image of the dimension
    M, N = f.shape[0], f.shape[1]
    #creation of the mask
    mask = (1 / (w * w) * (np.ones((w, w), dtype=np.int32)))
    #neighborhood of the distance pixels of the image border
    size_mask = (floor((w) / 2))
    #replication of padding with the neighborhood
    pad = imagePad4e(f, size_mask, size_mask, 'replicate')
    #copy the image original for receive the pixel
    image_filtered = f.copy()
    for rows in range(M):
        for columns in range(N):
            #positioning of the pixel with the neighborhood
            pad_img = pad[rows:rows + w, columns:columns + w]
            #achievement of all products between the elements of the filter with the corresponding neighborhood elements
            product = mask * pad_img
            #result of the pixel for the sum of the products
            image_filtered[rows, columns] = product.sum()
    return image_filtered
