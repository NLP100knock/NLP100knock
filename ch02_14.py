#coding:utf-8
"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""
"""
raw_input()でコマンドラインから文字列を入力することができる
※返される値はstrなので数値として扱う場合はintに変換する必要がある
"""
with open("data/hightemp.txt") as f:
	line = f.readlines()

print "先頭何行まで表示しますか？:",
num = raw_input()

for t in range(int(num)):
	print line[t],
