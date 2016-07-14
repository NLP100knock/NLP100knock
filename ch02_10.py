#coding:utf-8
"""
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

def countLines(file):
	f = open(file, "r")	
	
	lines = f.readlines() #file型をlist型に変換
	f.close()
	return len(lines)

if __name__ == "__main__":
	lines = countLines("data/hightemp.txt")

	print "行数は「%d行」です"%(lines)