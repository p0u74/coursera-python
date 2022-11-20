count = 0
my_file = open("mbox-short.txt")
for line in my_file:
    if not line.startswith("From"):
        continue
    word = line.split()
    if not len(word) > 2 :
        continue
    print(word[1])
    count += 1 
print("There were", count, "lines in the file with From as the first word")