month=int(input("Enter the month: "))
year=int(input("Enter the year: "))
if 1<= month <=12: 
    if 1900 <= year <=2025:       
        if month==4 or month==6 or month==9 or month==11:
            print(f"There are 30 days in {month} month")
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            print(f"There are 31 days in {month} month and {year} year")
        if month==2:
            if year%4==0:
                print(f"There are 29 days in {month} month and {year} year")
            elif year%100==0:
                print(f"There are 29 days in {month} month and {year} year")
            elif year%400==0:
                print (f"There are 29 days in {month} month and {year} year")   
        else: print(f"There are 28 days in {month} month and {year} year")    
    else: print ("Invalid data")            
else: print("Invalid data")            