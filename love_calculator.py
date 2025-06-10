name1=input("Enter your name: ")
name2=input("Enter your partner name: ")


name = name1 + name2
name_lower = name.lower()

t=name_lower.count('t')
r=name_lower.count('r')
u=name_lower.count('u')
e=name_lower.count('e')

l=name_lower.count('l')
o=name_lower.count('o')
v=name_lower.count('v')
e=name_lower.count('e')


true=(t+r+u+e)
love=(l+o+v+e)

print(f"your love score is {true}{love}%")