# -*- coding: utf-8 -*-

"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを
表示せよ．確認にはheadコマンドを用いよ．
"""

datafile = open('./data/hightemp.txt')

print('入力してください')
input_line = raw_input('>>>')

ngyou = []
for i in datafile:
    ngyou.append(i)

for i in range(int(input_line)):
    j = int(input_line) - i
    print ngyou[-j]

