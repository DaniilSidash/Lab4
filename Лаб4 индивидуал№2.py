#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Дана последовательность слов. Проверить, правильно ли в ней записаны буквосочетания
# ча и ща. Исправить ошибки.



if __name__ == '__main__':
    s = input('Введите слова: ')
    a = s.find('ча')
    b = s.find('чя')
    if a > -1:
        print('ча написанно правильно')
    if b > -1:
        print('ча написанно неправильно')
    c = s.find('ща')
    d = s.find('щя')
    if c > -1:
        print('ща написанно правильно')
    if d > -1:
        print('ща написанно неправильно')
    s = s.replace('чя', 'ча').replace('щя', 'ща')
    print(s)








