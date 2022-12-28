def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        a : float
        b : float
    '''
    #ingreso el valor de las variables a y b
    a=float(input("Ingrese el valor de la variable a:"))
    #while que no permite numeros negativos
    while(a<=0):
        print("No ingrese numeros negativos!")
        a=float(input("Ingrese el valor de la variable a:"))

    b=float(input("Ingrese el valor de la variable b:"))
    #while que no permite numeros negativos
    while(b<=0):
        print("No ingrese numeros negativos!")
        b=float(input("Ingrese el valor de la variable b:"))
    return a,b

def solucionarOperacionAritmetica(a,b):
    '''
    Funcion que resuelve la operacion aritmetica (a+b^2)/2.5

    Parametros:
    ------------
        a : float
        b : float

    Retorna:
    ------------
        solucion : float
    '''
    #resolviendo la operacion
    solucion = (a+(b**2))/2.5
    #retornamos solucion
    return solucion


if __name__ == '__main__':
    print("Resolver (a+b^2)/2.5")
    #leemos variables
    a,b=leer_variables()
    #el valor que retorne esta funcion se guarda en solucion
    solucion= solucionarOperacionAritmetica(a,b)
    

    #imprimo la solucion a la operacion aritmetica 
    print("la solucion a la operacion aritmetica (a+b^2)/2.5 es: ",solucion)