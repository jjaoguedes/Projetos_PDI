import statistics
from math import floor
from Projetos_PDI.project5_joao_felix_caroline_braz.imagePad4e import imagePad4e

def medianSFilter(f , w):

    #image of the dimension
    M, N = f.shape[0], f.shape[1]
    #neighborhood of the distance pixels of the image border
    size_mask = (floor((w) / 2))
    #replicamento de pad com a vizinhança
    pad = imagePad4e(f, size_mask, size_mask, 'replicate')
    #copy the image original for receive the pixel
    image_filtered = f.copy()
    for rows in range(M):
        for columns in range(N):
            #posicionamento do pixel com a vizinhança
            pad_img = pad[rows:rows + w, columns:columns + w]
            #transform on a one-dimensional array
            img_uni = pad_img.ravel()
            #convert for a list
            List = list(img_uni)
            #organize the elements of the list
            List.sort()
            #calculate the median of the list
            median = statistics.median(List)
            #result of the median for the pixel
            image_filtered[rows, columns] = median
    return image_filtered