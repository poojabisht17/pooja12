import random
print("Let's play Hangman!!\nYou have only 6 lives so try to guess the word within 6 attempts.\nGood luck!!!")
words=['apple', 'mango', 'pineapple', 'guava', 'lion', 'tiger', 'cow']
word=random.choice(words)
length_word=len(word)
i=0
while i<length_word:
    print("'_'", sep=",", end=".")
    i+=1
word_list=set(word)
#print(word_list)
letter=set(input("Guess the letter: "))
if letter<=word_list:
    print(letter)
#print(word)
