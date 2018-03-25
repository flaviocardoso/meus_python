#!/usr/bin/env python3

import os
from datetime import date
#init = time.time()

hj = date.today()
dia = str(hj)
pastas = dia.replace("-", "/")
pasta =  "../teste/{0}".format(pastas)
#t = "./teste/2018/03/23"
if not os.path.exists(pasta):
    os.makedirs(pasta)
