# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-03-23
    
"""
from sympy import *


x, y = symbols('x y')
print solve([2 * x + y * 6, 3 * y - 6 / x], [x, y])
print solve([2 * x - y - 3, 3 * x + y - 7],[x, y])
