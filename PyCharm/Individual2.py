#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    print("Введите координаты точки и радиус круга: ")
    x = float(input("x = "))
    y = float(input("y = "))
    r = float(input("R = "))

    R = math.sqrt(x ** 2 + y ** 2)

    if R <= r:
        print("Точка принадлежит кругу")
    else:
        print("Точка не принадлежит кругу")


