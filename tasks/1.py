#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    sentence = input('Enter sentence: ')
    index = 2
    for i, sent in enumerate(sentence):
        if i == index:
            print(sentence[index])
            index += 3
