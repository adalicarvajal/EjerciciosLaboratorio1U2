import math
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
        c : float
    '''
    #ingreso el valor de las variables a,b y c
    a=float(input("Ingrese el valor de la variable a:"))
    b=float(input("Ingrese el valor de la variable b:"))
    c=float(input("Ingrese el valor de la variable c:"))
    
    #retornamos la o las variables
    return a,b,c
def resolverExpresion(a,b,c):
    '''
    Funcion que resuelve la expresion (-b+raiz(b^2+c))/2a

    Parametros:
    ------------
        a : float
        b : float
        c : float

    Retorna:
    ------------
        solucion : float
    '''
    #resolviendo la expresion
    solucion = (-b+math.sqrt((b**2)+c))/(2*a)
    #retornamos la solucion
    return solucion
if __name__ == '__main__':
    print("Resolver (-b+raiz(b^2+c))/2a")
    #leemos variables
    a,b,c=leer_variables()
    #el valor que retorne esta funcion se guarda en potencia
    solucion = resolverExpresion(a,b,c)
    #imprimo la solucion
    print("(-b+raiz(b^2+c))/2a es: ",solucion)