import re
number = list()
text = open("regex_sum_1673439.txt")
for line in text :
    num = re.findall('[0-9]+',line) # match and extract numbers as string
    if num == [] : continue # skip empty lists
    for i in num :
        number.append(int(i)) # casting strings to integer and appending to our number list

print("sum :", sum(number)) # printing sum of our number list
    