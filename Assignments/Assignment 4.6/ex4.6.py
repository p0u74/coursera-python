def computepay(fhours, frate):
    if fhours > 40 :
        reg = fhours * frate
        overtime = (fhours - 40.0) * (frate * 0.5)
        xp = reg + overtime
    else :
        xp = fhours * frate
    return xp

hours = input("Enter hours : ")
rate = input("Enter rate : ")
try :
    fhours = float(hours)
    frate = float(rate)
except : 
    print("Error! please enter numeric input.")
    quit()
pay = computepay(fhours, frate)
print("Pay", pay)