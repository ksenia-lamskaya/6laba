#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Даны два слова. Определить, можно ли из букв первого из них получить второе. 
#Рассмотреть два варианта: 
#Повторяющиеся буквы второго слова могут в первом слове не повторяться; 
#Каждая буква второго слова должна входить в первое слово столько же раз, сколько и во второе.

if __name__ == "__main__":
    word1 = input("Введите первое слово: ")
    word2 = input("Введите второе слово: ")
    
    # Первый вариант
    flag = True
    for char in word2:
        if word1.count(char) == 0:
            flag = False
            break
    print(flag)
    # Второй вариант
    flag = True
    for char in word2:
        if word1.count(char) != word2.count(char):
            flag= False
    print(flag)
