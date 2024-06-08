import numpy as np

def imagePad4e(f, r, c, padtype):
    #image of the dimension
    height, width = f.shape[0], f.shape[1]

    #calculate the new height and width of the pad
    new_height = height + (2 * r)
    new_width = width + (2 * c)

    #create the array of the zeros for the padding
    f_pad = np.zeros((new_height, new_width), dtype=f.dtype)

    #put the original image a imagem original in the center of the zero pad
    for row in range(height):
        for column in range(width):
            f_pad[row + r][column + c] = f[row][column]

    if padtype == 'replicate':
        #replicates top and bottom borders
        for row in range(r):
            for column in range(new_width):
                f_pad[row][column] = f_pad[(2*r)-row-1][column]  #top border
                f_pad[new_height-1-row][column] = f_pad[new_height-(2*r)-1+row][column]  #bottom border
        # replicates left and right borders
        for row in range(new_height):
            for column in range(c):
                f_pad[row][column] = f_pad[row][(2 * c) - column + 1]  #left border
                f_pad[row][new_width-1-column] = f_pad[row][new_width-(2*c)-1-column]  #right border
    return f_pad
