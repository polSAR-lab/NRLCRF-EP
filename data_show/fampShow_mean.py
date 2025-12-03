import numpy as np
import matplotlib.pyplot as plt
import f_typical_visualize_yip



def fampShow_mean(data, n=2):
    type_val = 'mean'
    siz = np.shape(data)

    data = f_typical_visualize_yip.f_typical_visualize_yip(data, type_val)

    plt.figure()
    plt.imshow(data, cmap='gray')
    # plt.title('input data')
    plt.show()
