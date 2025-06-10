import random
name_data=[]
name=input("Enter the names of people(separated by space) who will pay the bill: ").split()
name_data.extend(name)
print(name_data)
bill_payer=random.choice (name_data)
print(f"Todays bill will be paid by {bill_payer}")
