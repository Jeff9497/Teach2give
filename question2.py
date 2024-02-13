# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.

def fibonacci():
    a, b = 0, 1
    while a < 100:
        print(a, end=' ')
        a, b = b, a + b

fibonacci()
