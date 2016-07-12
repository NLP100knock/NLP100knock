#coding:utf-8
"""
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""


str1 = "パトカー"
str2 = "タクシー"
str3 = ""

for t in range(len(str1)):
	str3 += str1[t] + str2[t]

print str3 
