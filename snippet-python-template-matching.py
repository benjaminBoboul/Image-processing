#!/usr/bin/env python
import cv2
import numpy as np

img_rgb = cv2.imread("./Data-TP/Template/image.jpg")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template_img = cv2.imread('Data-TP/Template/template.jpg', 0)

img_c = img_rgb.copy()
img = img_gray.copy()
print(template_img.shape)
w, h = template_img.shape

res = cv2.matchTemplate(img,template_img, cv2.TM_CCOEFF_NORMED)

threshold = 0.8
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_c, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img_c)
cv2.waitKey(0)
cv2.destroyAllWindows()