# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.
# Examples: 
# 8=> returns true
# 6=> returns false


def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Examples 
print(is_power_of_two(8))  # Output: True
print(is_power_of_two(6))  # Output: False

