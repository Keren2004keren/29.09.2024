import random

# START

# a
range_list: list[int] = [i for i in range(95, 106)]
print(range_list)

# b
even_list: list[int] = [i for i in range(10, 21, 2)]
print(even_list)

# c
random_list = [random.choice([True, False]) for _ in range(5)]
print(random_list)

# d
list_rand: list[int] = [random.randint(1, 100) for _ in range(10)]
print(list_rand)

# e
rand_list: list[int] = [i for i in list_rand if i > 50]
print(rand_list)

# f
random_one_line: list[int] = [i for i in [random.randint(1, 100) for _ in range(10)] if i > 50]
print(random_one_line)

# g
# string_user: str = (input("How was your day?: "))
# without_t_space: list[str] = []
# for letter in string_user:
#     if letter != "t" and letter != " ":
#         without_t_space.append(letter)
# print(without_t_space)
# in comprehension
string_user: str = (input("How was your day?: "))
without_t_space: list[str] = [letter for letter in string_user if letter != "t" and letter != " "]
print(without_t_space)

# h
random_10_99: list[int] = [random.randint(10, 99) for _ in range(10)]
print(random_10_99)

ahadot_list: list[int] = [num % 10 for num in random_10_99]
print(ahadot_list)

# STOP
