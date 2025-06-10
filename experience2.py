experience= int(input("Enter your experience: "))
if 0< experience <= 1:
        Manual_testing = input("Does your skill include Manual Testing (Y/N): ")
        if Manual_testing.lower() == 'y':
            print("You are eligible for Manual Testing")
        elif Manual_testing.lower()== 'n':
            print("Not eligible for any role") 
if 1<= experience <= 4:
        Python_Robot = input("Does your skill include Python & Robot framework (Y/N): ")
        if Python_Robot.lower() == 'y':
            print("You are eligible for Automation")  
        elif Python_Robot.lower() == 'n':   
            print("Not eligible for any role") 
if 4< experience <= 6:
        API_Mobile_Selenium = input("Does your skil include API testing, Mobile testing, Selenium (Y/N): ")
        if API_Mobile_Selenium.lower() == 'y':
            print("You are eligible for Full Stack QA")
        elif API_Mobile_Selenium.lower() == 'n':
            print("Not eligible for any role")    
print("Enter a valid data")
      
