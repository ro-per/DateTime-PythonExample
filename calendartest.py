import calendar

#check in a range, which years are leap years
for y in range(1990,2020):  
    print(str(y)+" "+str(calendar.isleap(y)))

