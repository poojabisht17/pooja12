pizza_size=(str(input("Enter the size of the Pizza: (Small/Medium/Large): ")))
pizza_price=0
pepperonni_price=0
Extra_cheeze=0
total_bill=0

if pizza_size=='small' or pizza_size=='Small':
    pizza_price=100
    
    pepperoni=(str(input("Would you like to add pepperoni (Y/N): ")))
    if pepperoni== 'Y' or pepperoni== 'y':
        pizza_price=pizza_price+30
    else: pizza_price=pizza_price

    extra_cheese=(str(input("Would you like to add Extra Cheese (Y/N): ")))
    if extra_cheese== 'Y' or extra_cheese=='y':
                pizza_price=pizza_price+20
    else: pizza_price=pizza_price  

if pizza_size=='medium' or pizza_size=='Medium':
    pizza_price=200
    
    pepperoni=(str(input("Would you like to add pepperoni (Y/N): ")))
    if pepperoni== 'Y' or pepperoni== 'y':
        pizza_price=pizza_price+50
    else: pizza_price=pizza_price

    extra_cheese=(str(input("Would you like to add Extra Cheese (Y/N): ")))
    if extra_cheese== 'Y' or extra_cheese=='y':
                pizza_price=pizza_price+20
    else: pizza_price=pizza_price  

if pizza_size=='large' or pizza_size=='Large':
    pizza_price=300
    
    pepperoni=(str(input("Would you like to add pepperoni (Y/N): ")))
    if pepperoni== 'Y' or pepperoni== 'y':
        pizza_price=pizza_price+50
    else: pizza_price=pizza_price

    extra_cheese=(str(input("Would you like to add Extra Cheese (Y/N): ")))
    if extra_cheese== 'Y' or extra_cheese=='y':
                pizza_price=pizza_price+20
    else: pizza_price=pizza_price      

print(f"Your total bill is {pizza_price}")
    
    
 