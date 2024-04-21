# Iteradores

Conjunto de elementos que debe permitir que se retornen sus elementos.
En python los objetos iterables sonaquellos que sepueden recorrer usando un ciclo entre ellos:

- Cadenas de texto
- Listas
- Tuplas
- Diccionarios

## Funciones para crear iteradores

- `iter()`: ecibe el objeto iterable, crea un iterador y de esta manera permite recorrer el conjunto de elementos u objeto iterable. 
- `next()` : Recibe el iterador creado y cada vez que se invoca retorna el elemento siguiente del objeto iterable.

### Creacion de iterador con iter


- Creamos nuestra lista a iterar.
- Creamos nuestro iterador por medio de iter 
- Ejecutamos la funcion next para recorrer el objeto.

Cuando ejecutamos next y ya no hay elementos para recorrer nos devuelve un error.

~~~
numbers = [1,2,3]
iteradtor = iter(numbers)

>>>next(iterator)
 1

>>>next(iterator)
2

>>>next(iterator)
3

>>>next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

~~~

No esmuy comun ver este tipo de creacion de iteradores , sin embargo esta funcion es usada como base de otras funciones como zip,map y filter.

# Funcion zip

Esta funcion crea un objeto iterable en el cual cada elemento es una tupla creadad a partir de otros objetos iterables.
Con esta funcion unimos uno o mas iterables y cada union es una tupla.

Para visualizar nuestra lista de elementos, convertimos el objeto zip devuelto en una lista utilizando el método list().
~~~
first_name = ['Jesus', 'Martha', 'Ana']
last_name =['Cruz', 'Estudillo', 'Garcia'] 

full_name = list(zip(first_name, last_name))

print(full_name)

# Valor devuelto

[('Jesus', 'Cruz'), ('Martha', 'Estudillo'), ('Ana', 'Garcia')]
~~~

- En cada tupla observaremos que se combinaron en su respectiva posicion, es decir la posicion 0 de ambas listas se almacenaron en una sola tupla y asi sucesivamente hasta que terminen los elementos.
- Si agregamos un elemento a alguna de nuestras listas no se crearan mas tuplas ya que el ultimo elemento on tienen una posicion respectiva en apellido por tanto no puede ser unida con un elemento.

## Desempaquetar listas

En Python, puedes realizar la operación de "unzip" utilizando la función zip() junto con el operador * (splat operator) en una lista de tuplas. 

- Sintaxis
```
tup = [(1, 'a'), (2, 'b'), (3, 'c')]

numbers, letters = zip(*tup)

print(numbers)  # Resultado: (1, 2, 3)
print(letters)   # Resultado: ('a', 'b', 'c')
```

- Desempaquetando nombres y apellidos

```
names, last_names = zip(*full_name)

print(names)            # Res ('Jesus', 'Martha', 'Ana')
print(last_names)       # Res ['Cruz', 'Estudillo', 'Garcia']

```

Al desempaquetar, se mantienen las posiciones de las tuplas originales en la lista zip. Esto significa que cada elemento en la posición 0 de la lista de nombres completos será parte de la tupla desempaquetada en la misma posición, y así sucesivamente.

## Iteracion sobre listas unidas

Para recorrer una lista anidada es muy similar a recorrer listas comunes, en este caso asignamos un nombre a cada valor que se va a iterar en este caso 

```
name = ['Juan', 'María', 'Carlos']
age = [30, 25, 35]

# Combinamos las listas utilizando zip
list_combination = list(zip(name, age))

# Recorremos la lista combinada
for el in list_combination:
    name, age = el
    print(f"{name} tiene {age} años.")

# Juan tiene 30 años.
# María tiene 25 años.
# Carlos tiene 35 años.
```

Esto nos sirve para procesos en donde debemos manejar multiples iterables al mismo tiempo.