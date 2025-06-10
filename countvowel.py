word=input("Enter any word: ").lower()
vowels = "aeiouAEIOU"
count = {i: word.count(i) for i in vowels if i in word}
print(f"There are {count} vowels in {word} ")    

