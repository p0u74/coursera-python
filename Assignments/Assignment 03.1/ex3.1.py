hours = input("Enter Hours : ")
rate = input("Enter Rate : ")
try : 
    fhours = float(hours)
    frate = float(rate)
except :
    print("Error! please enter numeric input.")
    quit()
if fhours > 40 :
    reg = fhours * frate
    overtime = (fhours - 40.0) * (frate * 0.5)
    xp = reg + overtime
else :
    xp = fhours * frate
print(xp)