def separate_even_and_odd(list_numbers):
    pair = []
    odd = []

    for number in list_numbers:
        if number % 2 == 0:
            pair.append(number)
        else:
            odd.append(number)

    return pair, odd



# ------- Expresion sencilla que se puede convertir a funcion lambda

def calc_square_area(side):
    return side ** 2
# ---  Funcion lambda

calc_square = lambda side: side ** 2

print(calc_square(2))

# ---------- CASOS DE USOS FUNCIONES LAMBDA
#Muchos desarrolladores de python recomiendan no utilizar las funciones lambda por que dificultan la lectura del codigo
#Estas funciones se utilizan mas que nada en conjunto de las funciones filter y map, para filtrar datos.

# --- FUNCION FILTER
# Recibe como primer parametro la funciuon anonima que define si un numero es par o impar y como segundo parametro la lista a afiltrar
#Toda esta funcion la envolvemos dentro de un tipo de dato list, ya que de otra forma nos devolvera el dato en crudo.

number_list = [1,2,3,4,5,6,7,8]
list_pairs = list(filter(lambda num: num % 2 == 0, number_list))

print(list_pairs)

# ---- FUNCION MAP

# Recibe dos argumentos
# ---- El primero es una funcion o una lambda
# ---- El segundo es un objewto iterablke al cual se aplicara la funcion

new_list = list(map(lambda number: number * 10, number_list))
print(new_list)


# Estos dos son los mas casos de usos en donde se utilizara una funcion lambda
