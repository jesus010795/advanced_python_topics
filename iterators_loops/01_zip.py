first_name = ['Jesus', 'Martha', 'Ana', 'Anahi']
last_name =['Cruz', 'Estudillo', 'Garcia'] 

full_name = list(zip(first_name, last_name))

print(full_name)



# ----- UNZIP

tup = [(1, 'a'), (2, 'b'), (3, 'c')]

numbers, letters = zip(*tup)

print(numbers)  # Resultado: (1, 2, 3)
print(letters)   # Resultado: ('a', 'b', 'c')


# ----- Desempaquetando nombres y apellidos

names, last_names = zip(*full_name)

print(names)            # Res ('Jesus', 'Martha', 'Ana')
print(last_names)            # Res ['Cruz', 'Estudillo', 'Garcia']



# ----- ITERAR SOBRE LISTAS UNIDASS

#   Ejemplo 1
for name , last_name in full_name:
    print(name, last_name)


#   Ejemplo 2
name = ['Juan', 'María', 'Carlos']
age = [30, 25, 35]

# Combinamos las listas utilizando zip
list_combination = list(zip(name, age))

# Recorremos la lista combinada
for el in list_combination:
    name, age = el
    print(f"{name} tiene {age} años.")
