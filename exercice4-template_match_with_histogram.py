#!/usr/bin/env python
import cv2
import numpy as np
import math
import pprint

img_rgb = cv2.imread("Data-TP/mon.jpg")
template_rgb = cv2.imread('Data-TP/statue.jpg')
img_size = img_rgb.shape[:2]
tmp_size = template_rgb.shape[:2]
y_steps = range(0, math.floor(img_size[0]/tmp_size[0]))
x_steps = range(0, math.floor(img_size[1]/tmp_size[1]))

"""
Issue with border : this doesn't process border if images shape doesn't correlate.
This will cause the script to ignore right and lower borders

Todo : add mask or resize image to fix this mess
"""

template_hist = cv2.calcHist(template_rgb, [2], None, [256], [0, 256]) # get template histogram
hist_cmp = {}
for y in y_steps:
    y_range = (tmp_size[0]*y, tmp_size[0]*y+tmp_size[0])
    for x in x_steps:
        x_range = (tmp_size[0]*x, tmp_size[0]*x+tmp_size[0])
        a = img_rgb[y_range[0]:y_range[1], x_range[0]:x_range[1]]
        #cv2.imshow("current_frame_{}_{}".format(y, x), a) # toggle this line if you want spaghetti windows
        img_hist = cv2.calcHist(a, [2], None, [256], [0, 256]) # get img_rgb histogram
        hist_cmp["{}_{}".format(y_range, x_range)] = cv2.compareHist(template_hist, img_hist, cv2.HISTCMP_CORREL)

pprint.pprint(hist_cmp)
print(max(hist_cmp.values()))

scope = list(hist_cmp.keys())[list(hist_cmp.values()).index(max(hist_cmp.values()))]
print(scope) # correlation coordinates
cv2.rectangle(img_rgb, (89, 0), (178, 89), (0, 255, 0), 2) # ok so logs outputs use the following format : (upper y, upper x)_(lower y, lower_x) while rectangle take (upper x, upper y), (lower x, lower y) in input
# need to find a way to store matches with their localisation in a proper format
cv2.imshow('result', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()