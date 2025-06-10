list1=["Hi", "Hello", "Welcome"]
names=["Krishna", "Ram" ,"Shiva"]
for item in list1:
    for name in names:
        print(item, name)
        if item=="Hello" and name=="Ram":
            break
    print("Out from inner loop")
print("Out from outre loop")        