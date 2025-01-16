#(C02) 8.Accept a list of words and return length of longest word.

# Accept a list of words as input
s = [i for i in input("Enter some words: ").split()]

# Find the longest word using max() and key=len
longest_word = max(s, key=len)

# Display the longest word and its length
print("Longest word:", longest_word)
print("Length of the longest word:", len(longest_word))
