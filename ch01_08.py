#coding:utf-8
"""
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""
"""
chr(i):整数iとなるような文字1字からなる文字列を返す．例えばchr(97)は文字列"a"を返す
ord(str):長さ1の与えられた文字列に対し，その文字列がunicodeオブジェクトならばUnicodeコードポイントをあらわす整数，8ビット文字列ならばそのバイトの値を返します．例えばord("a")は整数97を返します．


"""

def cipher(str):
    ans = ''
    for t in str:
        if 97 <= ord(t) <= 122: #ASCIIコードで97~122=a~zのこと
            ans += chr(219 - ord(t))
        else:
            ans += x
    return ans

s = "I couldn't believe that I could actually understand what I was reading : \
the phenomenal power of the human mind ."

print(cipher(s))