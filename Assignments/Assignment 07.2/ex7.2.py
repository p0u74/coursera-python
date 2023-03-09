plus = 0
c = 0
fname = input("Enter your file name please : ")
file = open(fname)
for line in file :
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    c = c + 1
    x = line.find(":")
    temp = float(line[x+2:])
    plus = plus + temp
res = (plus/c)
print("Average spam confidence:",res)
