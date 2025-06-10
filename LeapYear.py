year=int(input("Enter any year: "))
if year%4==0:
    print(f"{year} is a Leap year")
elif year%100==0:
    print(f"{year} is a Leap year")
elif year%400==0:
    print(f"{year} is a Leap year")

else:
    print(f"{year} is NOT a Leap year")
