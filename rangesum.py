start_num=int(input("Enter the start number: "))
end_num=int(input("Enter the end number: "))
sum=0
for i in range(start_num, end_num+1):
    sum+=int(i)
print(sum)