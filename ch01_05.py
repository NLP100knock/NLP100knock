# -*- coding: utf-8 -*-

def ngram(text, n):
    am = []
    for i in range(len(text)):
        am.append(text[i:n+i])
    return am

text = "I am an NLPer"
print ngram(text, 2)
print ngram(text.split(), 2)
