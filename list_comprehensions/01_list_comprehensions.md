# Utilizacion de funcion map

En este ejemplo elevaremos al cuadrado una lista de numeros por medio de un for y de una funcion creadd por nosotros que nos devuelve un numero elevado al cuadrado.

Dentro del for creamos una variable temporal que conteendra el cuadrado del numero sobre el que se esta ejecutando la iteracion pra psteriormente agregarlo a la lista de numeros elevados al cuadrado.

```
def calc_square(number):
    return number**2


list_n = [1,2,3,4,5,6,7,8,9]
square_numbers = []


for number in list_n:
    square = calc_square(number)
    square_numbers.append(square)


print(square_numbers)
```

La función **`map()`** en Python se utiliza para aplicar una función a cada elemento de un iterable (como una lista, tupla, etc.) y devuelve un iterador que produce los resultados. La sintaxis básica de map() es la siguiente:

`map(función, iterable)`

En nuestro ejemplo la funcion a aplicar es la funcion calc_square y el elemnto iterable es nuestra lis de numeros.

```
n_square = list(map(calc_square, list_n))
print(n_square)
```
Aplicaremos el metodo list ya que map nos devuleve un objeto de tipo map cuya sintaxis no es entendile para el ususario final, de esta forma convertimnos este objeto en una lista que si podemos entender.

# List Comprehension

Es una menra de ocnstruir lista u objetos iterables utilizandfo una sola linea de codigo.

**Sintaxis**

```
lista = [expresion(elemento) for elemento in objeto_iterable if condicion]

Para cada elemento dentro del iterable se 
agrega o guarda dicho elemento si se cumple una condicion.

```

Asignamos a una variable el resultado de alguna operacion con un elemento, en donde el elemento se extrae de una lista de elementos, opcionalemnte podemos agregar un condicional y si se cumple, este elemento sera devuelto y/o almacenado dentro de la variable.

Aplicaremos las list comprehension para hallar el cuadrado de un numero a partir de una lista de numeros.

```
list_n = [1,2,3,4,5,6,7,8,9]
square_list = [number**2 for number in list_n]
print(square_list)

//[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Como podemos observar tenemos el mismo resulta que ejecutando  el bucle for y la funcion map, pero con un mejor codigo y con una mejor lectura.

Agregaremos un condicional pra que unicamente almacenemos los numeros pares elevados al cuadrado.

```
square_list_pairs = [number**2 for number in list_n if number%2 == 0]
print(square_list_pairs)
//[4, 16, 36, 64]
```

**Utilizando funciones en list comprehensions**

Podemos utilizar funciones dentro de nuestras list comprehension.
- Definiremos una funcion que nos devuelve un numero elevado al cuadrado y una ucnion que nos devuelve numeros pares.

```

def square(number):
    return number**2

def is_pair(number):
    return number % 2 == 0

square_numbers= [square(number) for number in range(1,21) if is_pair(number)]

//[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

```

Podemos agregar un sentencia else para poder manipular de diferente manera nuestros datos, en este caso agregaremos un 0 por cada numero impar.

> Para la condicion else se vea aplicada tenemos que cambiar el orden del bucle y de la sentencia if:

`lista = [expresion(elemento) if condicion else sentencia for elemento in objeto_iterable]`

```
square_numbers_list = [square(number) if is_pair(number) else 0 for number in range(1,21) ]

print(square_numbers_list)

// [0, 4, 0, 16, 0, 36, 0, 64, 0, 100, 0, 144, 0, 196, 0, 256, 0, 324, 0, 400]
```


Las list comprehension son muy flexibles y permiten la creación rápida y concisa de listas en Python, lo que la hace muy útil en muchas situaciones.