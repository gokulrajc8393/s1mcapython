# (C02).6.Count the number of characters (character frequency) in a string.

from collections import Counter

s = input("Enter a string: ")

char_frequency = Counter(s)

print("Character Frequency:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")