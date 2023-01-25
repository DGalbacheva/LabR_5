#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    for num in range(100, 1000):
        a = num // 100
        b = (num % 100) // 10
        c = num % 10
        sum = a + b + c

        if sum % 7 == 0 and num % 7 == 0:
            print(num)