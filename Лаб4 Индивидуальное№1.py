#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Дано предложение. Составить программу, которая выводит все вхождения в предложение
# двух заданных символов.


if __name__ == '__main__':
     s = list(input('Напечатайте предложение: ').split())
     c = input('Введите символы: ')
for i in range(len(s)):
            if(c in s[i]): print (s[i])







