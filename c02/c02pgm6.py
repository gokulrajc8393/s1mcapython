# (C02).6.Count the number of characters (character frequency) in a string.

# Input the line from the user
l = input("Enter a line: ")

# Dictionary to store the frequency of each character
res = {}

# Loop through each character in the string
for char in l:
    char = char.lower()  # Convert character to lowercase to ensure case-insensitive comparison
    if char in res:
        res[char] += 1  # Increment count if character already exists in the dictionary
    else:
        res[char] = 1   # Add the character to the dictionary with a count of 1

# Display the frequency of each character
for char, count in res.items():
    print(f"'{char}': {count}")
