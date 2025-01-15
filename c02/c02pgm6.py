# (C02).6.Count the number of characters (character frequency) in a string.

# Input string
text = input("Enter a string: ")

# Dictionary to store character counts
char_count = {}

# Iterate over each character in the string
for char in text:
    if char in char_count:
        char_count[char] += 1  # Increment count if character is already in dictionary
    else:
        char_count[char] = 1  # Initialize count if character is encountered for the first time

# Print the character frequency
for char, count in char_count.items():
    print(f"'{char}': {count}")
