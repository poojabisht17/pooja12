burger=input("Select a burger (veg/non-veg): ").lower()
bill=0
if burger=="veg":
    bill=100
elif burger=="non-veg": 
    bill=150
else: print("Invalid data"){

    cheese=input("Would you like to add cheese (y/n): ").lower()
    if cheese=='y':
        bill+=15
    elif cheese=='n':
        bill=bill    
    else:print ("Invalid data")

    fries=input("Select the size of fries(S/M/L): ").lower()
    if fries=="s":
        bill+=50
    elif fries=="m":
        bill+=75
    elif fries=='l':
        bill+=100    
    else:print ("Invalid data")  
}      

print(f"Your total bill is {bill}")