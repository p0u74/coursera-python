c = 0
sum = 0.0
while True :
    num = input("Enter your number or 'done' : ")
    if num == "done" :
        break
    try : 
        sum = sum + float(num)
    except :
        print("Only enter number or 'done'!")
        continue
    c += 1
print("Total :",sum)
print("Count :",c)
print("Average :",sum/c)