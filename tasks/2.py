#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    sentence = input("Введите предложение: ")

    sentence_lower = sentence.lower()

    first_index = -1

    found = False

    for i, char in enumerate(sentence_lower[:-1]):
        if char + sentence_lower[i + 1] == 'чу' or char + sentence_lower[i + 1] == 'щу':
            first_index = i + 1 
            found = True
            break

    if found:
        print(f"Буквосочетание найдено, порядковый номер первой буквы {first_index}.")
    else:
        print("Буквосочетание не найдено.")