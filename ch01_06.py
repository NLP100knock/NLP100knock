#coding:utf-8
"""
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""
"""
bi-gramとは文章を2文字ずつに区切ったインデックスのことである
1文字ずつの場合はuni-gram
2文字ずつの場合はtri-gram
と呼ばれる．
これらを総称してN-gram
と呼ぶ
"""

str1 = "paraparaparadise"
str2 = "paragraph"


def bigram(str):
	list = []
	for t in range(len(str)-1):
		list.append(str[t:t+2])

	return list

x = set(bigram(str1))
y = set(bigram(str2))

print(x.union(y))
print(x.intersection(y))
print(x.difference(y))

print("se" in x)
print("se" in y)
