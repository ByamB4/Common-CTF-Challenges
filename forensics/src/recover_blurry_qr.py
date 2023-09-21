import cv2 as cv
import numpy as np

original = cv.imread('qr.png')

recovered = np.zeros(original.shape, dtype=np.uint8)
recovered.fill(255)

def paint(x, y, dark, im):
    if dark:
        im[30+x*10:30+x*10+10, 30+y*10:30+y*10+10] = [0, 0, 0]
    else:
        im[30+x*10:30+x*10+10, 30+y*10:30+y*10+10] = [255, 255, 255]

def difference(i, j, im):
    blurred = cv.GaussianBlur(im, (43, 43), 0)
    diff = blurred[30+i*10:30+i*10+10, 30+j*10:30+j*10+10, 0] - original[30+i*10:30+i*10+10, 30+j*10:30+j*10+10, 0]
    diff[diff>128] = 255-diff[diff>128]
    return diff.sum()

for i in range(0, 37):
    for j in range(0, 37):
        min_diff = difference(i, j, recovered)
        is_paint = False
        bruteforce = recovered.copy()

        for mask in range(0, 2**7):
            for ii, jj, c  in zip([0, 0, 0, 1, 1, 1, 2], [0, 1, 2, -1, 0, 1, 0], range(7)):
                ii += i
                jj += j
                if ii < 0 or ii >= 37 or jj < 0 or jj >= 37:
                    continue

                if mask & (1 << (c)):
                    paint(ii, jj, True, bruteforce)
                else:
                    paint(ii, jj, False, bruteforce)

            new_diff = difference(i, j, bruteforce)
            if new_diff < min_diff:
                min_diff = new_diff
                is_paint = mask & 1

        paint(i, j, is_paint, recovered)
        cv.imshow('recovered', recovered)
        cv.waitKey(10)

