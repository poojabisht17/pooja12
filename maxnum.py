def max(a,b,c):
    if a>b and b>c:
        return a
    elif b>a and b>c:
        return b
    else: return c

print("The maximum number is:", max(4, 5, 6))
   
#using built-in function
#def max_of_three(a, b, c):
    #return max(a, b, c)
