def check_experience(experience):
    if isinstance(experience, (int, float)):
        return "Valid input"
    else:
        print("Invalid input")

# Input experience
experience = input("Enter your experience: ")

# Validate input
if check_experience(experience) == "Valid input":
    experience = int(experience)

    if experience <= 1:
        Manual_testing = input("Does your skill include Manual Testing (Y/N): ")
        if Manual_testing.lower() == 'y':
            print("You are eligible for Manual Testing")

    elif 2 <= experience <= 4:
        Python_Robot = input("Does your skill include Python & Robot framework (Y/N): ")
        if Python_Robot.lower() == 'y':
            print("You are eligible for Automation")

    elif 5 <= experience <= 6:
        API_Mobile_Selenium = input("Does your skill include API testing, Mobile testing, Selenium (Y/N): ")
        if API_Mobile_Selenium.lower() == 'y':
            print("You are eligible for Full Stack QA")
        else:
            print("Not eligible for any role")
    else:
        print("Not eligible for any role")

else:
    print("Please enter a valid number.")
