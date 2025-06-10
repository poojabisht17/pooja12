a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
print(f"{a}\n{b}\n{c}")
matrix=[a,b,c]
address=input("Enter any address for 3x3 matrix (eg:23): ")
row=int(address[0])
col=int(address[1])
row_actual=matrix[row-1]
row_actual[col-1]='X'
print(f"{a}\n{b}\n{c}")
