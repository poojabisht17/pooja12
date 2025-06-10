num=int(input("Enter the number for which table to be printed: "))
mul=int(input("Enter the multipler till table to be printed: "))
print(f"Table of {num} till multipler {mul}")
for i in range (1,mul+1):
    mul=num*i
    print(f"{num} * {i} = {mul}")