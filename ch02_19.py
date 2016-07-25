# -*- coding: utf-8 -*-

"""
各行の壱列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcat，uniq，sortコマンドを用いよ．
"""

datafile = open('./data/hightemp.txt')

data = []
for line in datafile:
    result = line.split("\t")
    data.append(result[0])

freq = {}
for d in data:
    if d in freq:
        freq[d] += 1
    else:
        freq[d] = 1

for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print k, v

"""
確認用unixコマンド
cut -f1 hightemp.txt | sort | uniq -c | sort -r
"""