numlist=[23, 56, 76, 12, 5, -7, 100, 98, 76, 76, 56, 13, -7]
numlist.sort()
print (numlist)
disctinct_numbers = set(numlist)
print (f"Distinct list= {disctinct_numbers}")
print(f"Largest number in the list is {max(numlist)}")
print(f"Second largest numnber in the list is {numlist[-2]}")