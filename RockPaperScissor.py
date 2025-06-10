import random
import sys
user_choice=int(input("Choose Rock=0/Paper=1/Scissor=2: "))
option=[0, 1, 2]

computer_choice=random.choice(option)

print(f"Computer has chosen {computer_choice}")
if user_choice==computer_choice:
    print("Match draw")
elif user_choice==2 and computer_choice==0:
    print("You loose")
elif user_choice==0 and computer_choice==2:
    print("You loose2")    
elif (user_choice>computer_choice):
    print("You Win!!!")    
elif (user_choice<computer_choice):
    print("You loose")

