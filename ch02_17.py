# -*- coding: utf-8 -*-

"""
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはsort,uniqコマンドを用いよ．
"""

datafile = open('./data/hightemp.txt')

data = []
for line in datafile:
    result = line.split('\t')
    data.append(result[0])

ans = sorted(set(data))

for line in ans:
    print line