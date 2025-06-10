experience_input = input("Enter your experience: ").strip()

if (experience_input.replace('.', '', 1).isdigit() and experience_input.count('.') <= 1):
    experience = float(experience_input)

    if experience==0:
        print("No job available for 0 experience ")
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

    if experience>6:
        print("You are over-experience")  
else: print("Enter a valid data")              

      
