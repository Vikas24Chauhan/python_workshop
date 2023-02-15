# Create a function named ‘factor’ that can only accepts 1 argument. The function should return the factorial of that number.

num = input("Please enter the number :- ")
n = int(num)


def factor(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return n * factor(n-1)


print(factor(n))
