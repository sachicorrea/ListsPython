import funciones_listas as fl

# cummulative items in a list
lst = []
num = int(input('Enter number of item to include in the list: '))

for n in range(num):
  numbers = int(input("Enter a number: "))
  lst.append(numbers)

print("Cummulative elements of the list inserted is:")
print(fl.suma_acumulativa(lst))

# Pig Latin word translator - Change variable startsVowel for True if English words start with a vowel; otherwise False in file funciones_listas
wordsList = []
quantityWords = int(input('Enter number of words to include in the list: '))

for n in range(quantityWords):
  words = input("Enter an English word: ")
  wordsList.append(words)

print("Words translated to Pig Latin that start with vowels or consonants are:")
print(fl.traductor_pig_latin(wordsList))

# Algorith to extract fruits that start with the A vowel from a list
fruitsList = []
quantityFruits = int(input('Enter the number of fruits to include in the list: '))

for n in range(quantityFruits):
  words = input("Enter a fruit: ")
  fruitsList.append(words)

print("List of fruits that cointain vitamin A")
print(fl.identificador_frutas(fruitsList))