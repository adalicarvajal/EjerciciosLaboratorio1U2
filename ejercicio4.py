import math
def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        ladosCuadrado : float
        altura : float
    '''
    #ingreso el tamaño de los lados del cuadrado
    ladosCuadrado=float(input("Ingrese el tamaños de los lados del cuadrado(cm):"))
    #whille que no permite ingresar numeros negativos
    while(ladosCuadrado<=0):
        print("Ingrese numeros positivos!")
        ladosCuadrado=float(input("Ingrese el tamaños de los lados del cuadrado(cm):"))

    #ingreso la altura de la piramide
    altura=float(input("Ingrese la altura de la piramide(cm):"))
    #whille que no permite ingresar numeros negativos
    while(altura<=0):
        print("Ingrese numeros positivos!")
        altura=float(input("Ingrese la altura de la piramide(cm):"))
    return (ladosCuadrado,altura)
def calcularAristaLateral(ladosCuadrado,altura):
    '''
    Funcion que obtiene el area de un rectangulo

    Parametros:
    ------------
        ladosCuadrado : float
        altura : float

    Retorna:
    ------------
        aristaLateral : float
    '''
    #primero calculamos la diagonal con la siguiente formula D =raiz(lados^2)+(lados^2)
    diagonal =math.sqrt((ladosCuadrado**2)+(ladosCuadrado**2))
    #calculo semidiagonal / cateto
    semiDiagonal = diagonal/2
    #calculo la arista lateral
    incognitaArista = (semiDiagonal**2) + (altura**2)
    aristaLateral = math.sqrt(incognitaArista)
    #retornamos el valor de la arista
    return aristaLateral

if __name__ == '__main__':
    print("Arista lateral de una piramide")
    #leemos variables
    ladosCuadrado,altura=leer_variables()
    #el valor que retorne esta funcion se guarda en aristaLateral
    aristaLateral=calcularAristaLateral(ladosCuadrado,altura)
    #imprimo la arista lateral
    print("La arita lateral de la piramide es: ",aristaLateral)