l1=list(map(int,input("Enter List 1: ").split()))
l2=list(map(int,input("Enter List 2: ").split()))
l3=[]
for n in range (len(l1)):
    sum=l1[n]+l2[n]
    l3.append(sum)
print(sum)
print(l1)
print(l2)
print(l3)
