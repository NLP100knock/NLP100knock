# -*- coding: utf-8 -*-
'''
12で作ったcol1.txtとxol2.txtを結合し、元ファイルの1列目と2列目をタブ区切りで並べた
テキストファイルを作成せよ．確認にはpasteコマンドを用いよ.
'''


datafile = open('./data/col1.txt')
datafile2 = open('./data/col2.txt')

f = open('col12.txt', 'w')

w1 = []
w2 = []

for line in datafile:
    w1.append(line.split('\n')[0])

for line in datafile2:
    w2.append(line)

for i in range(len(w1)):
    f.write(w1[i] + '\t' + w2[i])

f.close()


