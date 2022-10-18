score = input("Enter your score between 0.0 and 1.0 : ")
try : 
    fscore = float(score)
    fscore >= 0.0 and fscore <= 1.0
except : 
    print("Error! Enter numeric input between 0.0 and 1.0")
    quit()
if fscore >= 0.9 :
    print("A")
elif fscore >= 0.8 :
    print("B")
elif fscore >= 0.7 :
    print("C")
elif fscore >= 0.6 :
    print("D")
else :
    print("F")