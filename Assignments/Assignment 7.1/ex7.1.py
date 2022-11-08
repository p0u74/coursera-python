fname = input("Enter your file name : ")
try :
    fdata = open(fname)
except :
    print("Enter your file name : ")
    quit()
for line in fdata:
    line = line.rstrip()
fstring = fdata.read()
print(fstring.upper())