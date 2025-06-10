username="pooja"
password="Pooja@25"
count=0
actual_username=input(("Enter Username: "))
actual_password=input(("Enter Password: "))
while count <3: 

    if username==actual_username and password==actual_password:
        print("Login successful")
        break
    else: print ("Incorrect username/password. Try again.")  
count+=1
