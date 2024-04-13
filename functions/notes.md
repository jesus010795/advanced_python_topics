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