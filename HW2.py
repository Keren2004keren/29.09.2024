# START

# a
# try-except is a function that helps us to deal with errors, you ask python to try a function, and then you tell it
# except which says to the program that if an error is appearing don't let the program collapse.

# b
# you should catch to errors in python in order to make sure that your program wouldn't collapse during its run.

# c
try:
    trial = 88 / 0
except ZeroDivisionError:
    print("cannot divide by zero")

# d
try:
    age: int = int(input("Enter age: "))
    if not 1 <= age <= 110:
        raise ValueError(f"{age} is false")
except ValueError as e:
    print(e)

# e
import random

numbers_list: list[int] = []
for _ in range(4):
    numbers_list.append(random.randint(1, 20))
print(numbers_list)
while True:
    try:
        num: int = int(input("enter a number:"))
        if num == -999:
            break
        index = int(num)
        numbers_list[index] = num
        print(f"The updated list is {numbers_list}")
    except ValueError:
        print("The input is not valid, try again")
    except IndexError as e:
        print(f"the index {index} is out of range")

# STOP
