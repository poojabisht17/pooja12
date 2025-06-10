n=input("Enter any string: ")
#using list
# if str(n) == str(n)[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#using reverse function
rev = ''.join(reversed(n))

if n == rev:
    print("Palindrome")
else:
    print("Not a palindrome")