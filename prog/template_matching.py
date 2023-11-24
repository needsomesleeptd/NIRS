import cv2
import numpy as np
from matplotlib import pyplot as plt
src = cv2.imread(r'./images/arrows.png', cv2.IMREAD_COLOR)
img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
img1 = img.copy()
template = cv2.imread(r'./images/smth.png', cv2.IMREAD_GRAYSCALE)
h, w = template.shape[:]
# match methods
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for meth in methods:
    img2 = img1.copy()
    img3 = src.copy()
    method = eval(meth)
    res = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # if method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img2, top_left, bottom_right, 255, 2)
    cv2.rectangle(img3, top_left, bottom_right, (0, 0, 255), 2)
    # show result
    titles = ['Соответствие', 'Изображение', 'Результат']
    images = [res, img2, img3[:, :, ::-1]]
    plt.figure(figsize=(6, 3))
    for i in range(len(images)):
        plt.suptitle(meth)
        plt.subplot(1, 3, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.savefig(meth+'.png')
    plt.show()