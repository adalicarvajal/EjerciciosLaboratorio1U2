import math
def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        altura : float
        baseSuperior : float
        baseInferior : float
    '''
    #ingreso la altura del trapezoide
    altura=float(input("Ingrese la altura del trapezoide(cm):"))
    #while que no permite numeros negativos
    while(altura<=0):
        print("Solo ingrese numeros positivos")
        altura=float(input("Ingrese la altura del trapezoide(cm):"))
    
    #ingreso la base superior del trapezoide
    baseSuperior=float(input("Ingrese la base superior del trapezoide(cm):"))
    #while que no permite numeros negativos
    while(baseSuperior<=0):
        print("Solo ingrese numeros positivos")
        altura=float(input("Ingrese la base superior del trapezoide(cm):"))
    
    #ingreso la base superior del trapezoide
    baseInferior=float(input("Ingrese la base inferior del trapezoide(cm):"))
    #while que no permite numeros negativos
    while(baseInferior<=0):
        print("Solo ingrese numeros positivos")
        baseInferior=float(input("Ingrese la base inferior del trapezoide(cm):"))

    return (altura,baseSuperior,baseInferior)

def calcularAreaDelTrapezoide(altura,baseSuperior,baseInferior):
    '''
    Funcion que obtiene el area de un trapezoide

    Parametros:
    ------------
        altura : float
        baseSuperior : float
        baseInferior : float

    Retorna:
    ------------
        areaTrapezoide : float
    '''
    #resolviendo la formula para obtener el area del trapezoide
    areaTrapezoide =((1/2)*altura)*(baseSuperior+baseInferior)
    #retornamos el area del trapezoide
    return areaTrapezoide

if __name__ == '__main__':
    print("Hallar el area de un trapezoide")
    #leemos variables
    altura,baseSuperior,baseInferior=leer_variables()
    #el valor que retorne esta funcion se guarda en areaTrapezoide
    areaTrapezoide= calcularAreaDelTrapezoide(altura,baseSuperior,baseInferior)
    #imprimo el area del trapezoide
    print("El area del trapezoide es: ",areaTrapezoide)