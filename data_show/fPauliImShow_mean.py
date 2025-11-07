import numpy as np
import matplotlib.pyplot as plt
import f_typical_visualize_yip

def f_pauli_im_show_mean(data, n=2):
    type_val = 'mean'
    siz = np.shape(data)

    if siz[0] == 3:
        z = np.zeros_like(data[0, 0, :, :])
        z[:, :, 0] = f_typical_visualize_yip(data[0, 0, :, :], type_val)
        z[:, :, 1] = f_typical_visualize_yip(data[1, 1, :, :], type_val)
        z[:, :, 2] = f_typical_visualize_yip(data[2, 2, :, :], type_val)
    elif siz[2] == 3:
        z = np.zeros((siz[0], siz[1], siz[2]))
        z[:, :, 2] = f_typical_visualize_yip.f_typical_visualize_yip(data[:, :, 0, 0], type_val)
        z[:, :, 0] = f_typical_visualize_yip.f_typical_visualize_yip(data[:, :, 1, 1], type_val)
        z[:, :, 1] = f_typical_visualize_yip.f_typical_visualize_yip(data[:, :, 2, 2], type_val)
    elif siz[2] == 9:
        z = np.zeros_like(data[:, :, 0])
        z[:, :, 0] = f_typical_visualize_yip(data[:, :, 0], type_val)
        z[:, :, 1] = f_typical_visualize_yip(data[:, :, 1], type_val)
        z[:, :, 2] = f_typical_visualize_yip(data[:, :, 2], type_val)
    else:
        print('error')

    plt.figure()
    plt.imshow(z)
    plt.title('input data')
    plt.show()

