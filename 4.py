# Take two user inputs and pass those input variables in a try block. if the user input is 0, then throw the ZeroDivisionError exception

try:
    num1 = input("Please enter the 1st number :- ")
    num2 = input("please enter the 2nd number :- ")
    user1 = int(num1)
    user2 = int(num2)
    if user2 == 0:
        raise ZeroDivisionError
    else:
        ans = user1/user2
        print(f"the output is :- {ans}")
except ZeroDivisionError:
    print(f"something wrong {ZeroDivisionError}")
