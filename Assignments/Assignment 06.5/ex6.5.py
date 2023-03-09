text = "X-DSPAM-Confidence: 0.8475"
x = text.find(" ")
word = float(text[x+1:])
print(word)