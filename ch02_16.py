#coding:utf-8
"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""
"""
1ファイルに何行を入れるかがポイント
"""
import math

with open("data/hightemp.txt") as f:
	line = f.readlines()

print "ファイルを何分割しますか？",
num = int(raw_input())
loop = 0

if len(line) % num != 0:
	print ("hello")
	loop = len(line)/num + 1
else:
	print ("hell")
	loop = len(line)/num

for t in range(loop):
	with open("data%s.txt"%(t), "w") as f:
		f.writelines(line[num*t:num*(t+1)])






