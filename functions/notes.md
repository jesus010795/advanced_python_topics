# Orden de parametros
Las funciones reciben tres tipos de parametros, los primeros son datos definidos que nos permiten enviar parametros desde la funcion, los parametros especiales como los args cuando no tenemos conocimientos de la cantidad de datos a procesar o los kwargs cuando queremos definir nuevos parametros que no estan definidos dentro de la funcion.

Es importante respetar el orden de los parametros con el fin de evitar errores de sintaxis:
- En primer lugar tiene que ir los parametros definidos.
- Los ***args**
- Por ultimo los ****kwargs**

~~~
def ordered_parameters(name, last_name, *args, **kwargs):
    pass
~~~

# Funciones lambda
## Lenguaje lamnda
- Es un lenguaje basado en la abstraccion
- Creado por alonzo Chuch en 1930
- Minimalista: Exprension sencilla en una sola linea
## Programacion lambda
- Es un tipo de programacion funcional
- Esta construida de una sola expresion
- Puede tomar mas de un argumento
### Declarando funcion lambda en python
Esta es  la manera mas sencilla de declarar una funcion lamda
~~~
lambda x:x
~~~
-- lambda: Es la sentencia que invoca la funcion 
-- Primera **x** : Variable dependiente
-- Segunda **x**: Cuerpo de la funcion

# Funciones anonimas
Estas funciones reciben un nombre diferente en cada lenguaje.
En el caso de python las llamamos **funciones lambda** y se declaran a traves de la sentencia **lambda**
``lambda argumentos: expresion``
- Ejemplo de funcion sencilla
~~~
lambda num: num * 2

invocacion
>>>_(2)
4
~~~
Esta no es la forma mas practica de ejecutar una funcion lambda pero es solo para ejemplificar. 
 - Podemos asignar una funcion lambda a una variable y ejecutarla.
~~~
mult = =lambda num: num * 2
mult(3) -> 6
mult(2) -> 4
~~~