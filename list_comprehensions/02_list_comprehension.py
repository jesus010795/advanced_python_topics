def square(number):
    return number**2

def is_pair(number):
    return number % 2 == 0


list_n = [1,2,3,4,5,6,7,8,9]
square_numbers = []


# for number in list_n:
#     square = calc_square(number)
#     square_numbers.append(square)


# print(square_numbers)


square_list = [number**2 for number in list_n]
square_list_pairs = [number**2 for number in list_n if number%2 == 0]
print(square_list)
print(square_list_pairs)


# square_numbers_list = [square(number) for number in range(1,21) if is_pair(number)]


square_numbers_list = [square(number) if is_pair(number) else 0 for number in range(1,21) ]

print(square_numbers_list)