# START
try:
# a
    num1: int = int(input("Enter a four digit number: "))
    right_digit: int = num1 % 10
    print(f"The right digit is {right_digit}")

# b
    num2: int = int(input("Enter a four digit number:"))
    second_right: int = (num2 // 10) % 10
    print(f"The second right number is {second_right}")

# c
    num3: int = int(input("Enter a two digit number: "))
    left_digit3: int = num3 // 10
    right_digit3: int = num3 % 10
    print(f"The sum of the two digits is {right_digit3 + left_digit3}")

# d
    num4: int = int(input("Enter a two digit number: "))
    left_digit4: int = num4 // 10
    right_digit4: int = num4 % 10
    print(f"The reversed number is {(right_digit4 * 10) + left_digit4}")
# e
    num_list: list[int] = []
    for i in range(5):
        number: int = int(input("Enter a number: "))
        num_list.append(number)
    max_num: int = max(num_list)
    highest_value: int = num_list.index(max_num) + 1
    print(f"The highest value is in place {highest_value}")

except ValueError:
    print("Not a valid entry")

# STOP
