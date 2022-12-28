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
    #ingreso el valor de las variables X y Z
    x=float(input("Ingrese el valor de la variable x:"))
    z=float(input("Ingrese el valor de la variable y:"))
    
    #retornamos la o las variables
    return x,z
def resolverExpresion(x,z):
    '''
    Funcion que resuelve la expresion y=x^2+z^2

    Parametros:
    ------------
        x : float
        z : float

    Retorna:
    ------------
        y : float
    '''
    #resolviendo la expresion
    y = (x**2)+(z**2)
    #retornamos y
    return y
if __name__ == '__main__':
    print("Calcular y=x^2+z^2")
    #leemos variables
    x,z=leer_variables()
    #el valor que retorne esta funcion se guarda en potencia
    y = resolverExpresion(x,z)
    #imprimo la solucion
    print("y=x^2+z^2 es: ",y)