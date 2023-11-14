#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    word = input('Введите слово со знаком "." в конце: ')
    if word[-1] == '.':
        num = int(input('Введите порядковый номер буквы: '))
        a = input('Введите букву: ')
        for i, char in enumerate(word):
            if i == num:
                new_word = word[:i] + a + word[i:-1]
                print(f'Новое слово: {new_word}')
    else:
        print('В конце слова нет знака "."')