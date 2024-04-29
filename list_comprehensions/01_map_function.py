def calc_square(number):
    return number**2


list_n = [1,2,3,4,5,6,7,8,9]
square_numbers = []


for number in list_n:
    square = calc_square(number)
    square_numbers.append(square)


# print(square_numbers)



n_square = list(map(calc_square, list_n))
print(n_square)
