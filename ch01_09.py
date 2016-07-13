# -*- coding: utf-8 -*-

def irekae(text):
    import random
    texts = text.split()
    te = []
    for i in range(len(texts)):
        if (len(texts[i])) <= 4:
            te.append(texts[i])
        else:
            x = texts[i][1:-1]
            t = random.sample(x, len(x))
            x = texts[i][0] + ''.join(t) + texts[i][-1]
            te.append(x)
    return ' '.join(te)

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print irekae(text)