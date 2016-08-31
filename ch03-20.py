# coding: utf-8

import json


temp = {}

f = open('./data/jawiki-country.json', 'r')
i = 0

for line in f:
    temp[i] = json.loads(line)
    i += 1

f.close()

for k1, v1 in temp.iteritems():
    if temp[k1]["title"] == u"イギリス":
        print temp[k1]["text"]
        break