mydic = dict()
bigcount = None
bigword = None
file = open("mbox-short.txt")
for line in file :
    if not line.startswith("From") :
        continue
    # line = line.split()
    tem = line.split()
    if len(tem) > 2 :
        continue
    word = tem[1]
    mydic[word] = mydic.get(word,0) + 1

for key,count in mydic.items() :
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count

print(bigword,bigcount)
# print("counts : ", mydic)
# print("bigword : ", bigword)
# print("bigcount : ", bigcount)