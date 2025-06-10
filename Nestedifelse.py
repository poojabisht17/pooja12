height=float(input("Enter your height: "))


if height>3:
    print ("You can ride")
    bill=0
    age=int(input("Enter your age: "))
    if age<=12:
        #print("You need to Rs. 150")
        bill=150
    elif age<=18:
        #print("You need to pay Rs. 350")
        bill=350
    else:
    #print("You need to pay Rs. 500")
        bill=500

    want_photo=(str(input("Do you want to take photo? (Y?/N): ")))
    if want_photo=='y' or want_photo== 'Y':
    
            bill = bill+50

            print(f"Your total bill is {bill} ")
    else: 
        bill = bill
        print(f"Your total bill is {bill}")                


else: print("You cant ride")


