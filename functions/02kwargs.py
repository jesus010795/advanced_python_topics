# Los parametros kwargs son para metros especiales que nos permiten
# - Enviar datos no declarados a funciones en forma de llave y ValueError
# - Son argumentos de palabra clave

# -- Al imprimir la variable kwargs observaremos que se trata de un diccionario, por tanto al invocarla sera necesario
#    mandar la clave y el valor del parametro a utilizar

# --  Podemos iterar solbre los valores de kwargs y hacer con estos valores cualquier cosa
#     En este caso unicamente imprimiremos las claves y valores.

# --  Si sabemos lo que vamos a recibir dentro de nuestra funcion, podemos acceder a cada valor dentro de kwargs  
#     Por medio de notacion de llave indicamos cual es la variable que queremos manipular.


def func_kwargs(**kwargs):
    # print(kwargs)

    for key, value in kwargs.items():
        print(f"Clave: {key}, Valor: {value}")

    print(kwargs["nombre"])         # Jesus  
    print(kwargs["apellido"])       # Cruz

func_kwargs(nombre="Jesus", apellido="Cruz")