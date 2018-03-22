#!/usr/bin/env python

import numpy as np
import cv2
import glob

mages = glob.glob('*.jpg')

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    print(gray)
