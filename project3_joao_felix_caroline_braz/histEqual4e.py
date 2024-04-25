import numpy as np

def histEqual4e(f):

    #cálculo da probabilidade acumulada
    probability_accumulated = []
    sum_probability = 0
    for k in range(256):
        if k == 0:
            pass
        else:
            sum_probability += f[k-1]
        probability_accumulated.append(sum_probability)

    #mapeamento dos respectivos valores de cinza em novos valores equalizados.
    new_value_f = []
    for j in range(256):
        new_value = 255 * probability_accumulated[j]
        new_value_f.append(np.ceil(new_value))
    return np.array(new_value_f)
