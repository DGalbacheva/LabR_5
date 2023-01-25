#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    m = int(input("Введите номер месяца: "))

    print("Первое полугодие" if m in range(1,7) else "Второе полугодие")

    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        print("Месяц имеет 31 дня")
    elif m == 2:
        print("Месяц имее 28 дней")
    else:
        print("Месяц имеет 30 дней")