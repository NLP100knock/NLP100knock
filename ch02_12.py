#coding:utf-8
"""
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

import sys

with open("data/hightemp.txt") as f:
	line = f.readlines()
col = []
col1 = open("col1.txt", "w")
col2 = open("col2.txt", "w")
with open("col1.txt", "w") as col1, open("col2.txt", "w") as col2:
	for t in line:
		s = t.split("\t")
		col1.write(s[0] + "\n")
		col2.write(s[1] + "\n")




