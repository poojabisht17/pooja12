height=[]
heightsum=0
count=0
height=input("Enter the list of height separated by comma: ").split(",")

for i in height:
    heightsum+=int(i)
    count+=1
    #print(heightsum)
    #print(count)

average=(heightsum/count)
print(int(average))