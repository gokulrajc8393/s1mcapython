#(C02)4.Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square

import math

# Function to check if all digits of a number are even
def all_even_digits(num):
    return all(int(digit) % 2 == 0 for digit in str(num))

# Generate four-digit perfect square numbers with all even digits
result = []

for num in range(1000, 10000):
    if math.isqrt(num)**2 == num and all_even_digits(num):
        result.append(num)

print(result)


