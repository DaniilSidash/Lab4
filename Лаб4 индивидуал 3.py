#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Дано ошибочно написанное слово ИТЕРНЕТН. Путем перемещения его букв получить слово
# ИНТЕРНЕТ.

if __name__ == '__main__':
    word= "ИТЕРНЕТН"
    print(word[0]+word[7:]+word[-2]+word[-3]+word[-5]+word[-1]+word[-3]+word[-2] )

