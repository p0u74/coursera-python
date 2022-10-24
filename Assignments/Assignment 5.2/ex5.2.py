large = None
small = None
while True :
    num = input("Enter your number or 'done' : ")
    if num == "done" :
        break
    try : 
        fnum = int(num)
    except :
        print("Only enter number or 'done'!")
        continue
    # calculate maximum number
    if large is None :
        large = fnum
    elif fnum > large :
        large = fnum
    # calculate minimum number
    if small is None :
        small = fnum
    elif fnum < small :
        small = fnum
print("Largest :",large)
print("Smallest :",small)
