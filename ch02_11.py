# -*- coding: utf-8 -*-
'''
タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''


datafile = open('./data/hightemp.txt')

for line in datafile:
    print line.replace('\t', ' ')

