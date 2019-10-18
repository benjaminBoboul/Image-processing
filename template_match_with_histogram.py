#!/usr/bin/env python
import cv2
import numpy as np

img_rgb = cv2.imread("Data-TP/mon.jpg")
template_rgb = cv2.imread('Data-TP/statue.jpg')

img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
template_rgb = cv2.cvtColor(template_rgb, cv2.COLOR_BGR2RGB)

img_hist = cv2.calcHist(img_rgb, [2], None, [256], [0, 256]) # get img_rgb histogram
template_hist = cv2.calcHist(template_rgb, [2], None, [256], [0, 256]) # get template histogram

cv2.normalize(template_hist, img_hist)

result = cv2.compareHist(template_hist, img_hist, cv2.HISTCMP_INTERSECT)


print("== histogram comparison ==\n%e\n==========================" % result)
