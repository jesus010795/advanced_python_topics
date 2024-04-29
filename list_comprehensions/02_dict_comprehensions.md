# Dict comprehension

Son una forma concisa y eficiente de crear diccionarios. Funcionan de manera similar a las comprensiones de listas, pero en lugar de crear listas, crean diccionarios.

La sintaxis básica de una comprensión de diccionario es la siguiente:

`{clave: valor for elemento in iterable}`


Donde:

- Clave es la clave que se utilizará en cada par clave-valor en el diccionario.
- Valor es el valor correspondiente a cada clave.
- Elemento es una variable que toma cada valor del iterable.
- Iterable es la secuencia de elementos sobre la cual se itera (por ejemplo, una lista, tupla, rango, etc.).

Puedes también agregar condiciones para filtrar los elementos que se agregarán al diccionario, utilizando la siguiente sintaxis:

`{clave: valor for elemento in iterable if condición}`

```
dict_squares = {number: number**2 for number in range(1,11) if number %2 == 0 }
print(dict_squares)

# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

```