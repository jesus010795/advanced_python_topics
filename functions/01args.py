# En esta funcion calculamosel perimetro de una figura geometrica con 4 lados.

# -- Limitaciones
#     Esta forma de declarar la funcion nos limita a unicamentefiguras de 4lados
#     No es facil de reutilizar

# -- Mejoras
#     Utilizando la variable especial *args extenderemosla funcionalidad de la funcion
#     Este parametro sera recorrido con un for que nos permitira iterar sobrecada uno de los valores que se encuentran dentro de args

#Con la nueva funcion podemos calcular el perimetro de diferentes figuras
#si hacemos un print de args observaremos que nos devuelve una tupla conlos valores pasados por parametros.
  

def calc_perimeter(p1,p2,p3,p4):
    perimeter = p1 + p2 +p3 + p4
    return perimeter

some_per = calc_perimeter(1,2,3,4)
print(some_per)

def calc_perimeter_w_args(*args):
    perimeter = 0
    for p in args:
        perimeter += p

    return perimeter

another_per = calc_perimeter_w_args(1,2,3,4)
print(another_per)

per = calc_perimeter_w_args(1,2,3,4,5,6,7,8,9)
print(per)

