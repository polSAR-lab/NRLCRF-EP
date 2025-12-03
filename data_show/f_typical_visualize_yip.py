import numpy as np



def f_typical_visualize_yip(img, type_val):
    img[np.isnan(img)] = 0
    vector_img = img.flatten()
    vector_img = vector_img[vector_img != 0]

    if type_val == 'mean':
        IM = img / np.mean(vector_img) / 5
        IM[IM > 1] = 1
    elif type_val == 'log':
        IM = np.log1p(img)
        IM = IM / np.mean(IM)
        IM[IM > 1] = 1
    else:
        IM = img

    IM = np.round(IM * 255) / 255
    return IM
