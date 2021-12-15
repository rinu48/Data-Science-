#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:28:22 2021

@author: sjcet
"""

#9. Demonstrate the use of diag() function in 1D and 2D array.

import numpy as np

array_1d=np.arange(1,6).reshape((1,5))
print("1D array\n",array_1d)
print("use of diag() function in 1D array.")
x=np.diag(array_1d)
print(x,"\n")

array_2d=np.arange(9).reshape((3,3))
print("2D array\n",array_2d)
print("use of diag() function in 2D array.")
y=np.diag(array_2d)
print(y)