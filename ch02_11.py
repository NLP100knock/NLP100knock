# -*- coding: utf-8 -*-

datafile = open('hightemp.txt')

for line in datafile:
    print line.replace('\t', ' ')
