import math
def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        x : float
        z : float
    '''
    #ingreso la variable x
    x=float(input("Ingrese el valor de la variable x:"))

    #ingreso la variable z
    z=float(input("Ingrese el valor de la variable z:"))
    return (x,z)
def resolverExpresion(x,z):
    '''
    Funcion que resuelve la expresion y=(x^z)/2

    Parametros:
    ------------
        x : float
        z : float

    Retorna:
    ------------
        y : float
    '''
    #resolviendo la expresion 
    y = (x**z)/2
    #retornamos el valor de y
    return y

if __name__ == '__main__':
    print("Calcular la expresion y=(x^z)/2")
    #leemos variables
    x,z=leer_variables()
    #el valor que retorne esta funcion se guarda en expresionResuelta
    expresionResuelta=resolverExpresion(x,z)
    #imprimo la expresion resuelta
    print("La expresion resuelta es: ",expresionResuelta)