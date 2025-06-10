import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols=['!', '@', '#', '$', '%', '^', '&', '*',]
numbers=[0,1,2,3,4,5,6,7,8,9]
letter_count=int(input("How many letter would you like in your password: "))
symbol_count=int(input("How many symbol would you like in your password:" ))
number_count=int(input("How many number would you like in your password:" ))
pass_letter=random.sample(letters, letter_count)
pass_symbol=random.sample(symbols, symbol_count)
pass_number=random.sample(numbers, number_count)

password=pass_letter+pass_symbol+pass_number
random.shuffle(password)
password1=''
for r in password:
    password1+=str(r)
print(password1)