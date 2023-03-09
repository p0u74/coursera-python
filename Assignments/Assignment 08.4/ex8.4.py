my_list = list()
text = open("romeo.txt")
for line in text :
    line_list = line.split()
    for word in line_list :
        if word in my_list :
            continue
        my_list.append(word)
my_list.sort()
print(my_list)