count = dict()
file = open("mbox-short.txt")
for line in file :
    if not line.startswith("From") :
        continue
    sline = line.split()
    if len(sline) < 3 :
        continue
    time = sline[5]
    hour = time[:2]
    count[hour] = count.get(hour, 0) + 1 # counting how many times hour repeated

sort = sorted([(k,v) for k,v in count.items()])
for k,v in sort : # printing sorted hour and repeated
    print(k,v)