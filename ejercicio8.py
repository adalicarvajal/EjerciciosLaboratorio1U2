import math
def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        radio : float
    '''
    #ingreso el radio del circulo
    radio=float(input("Ingrese el radio del circulo(m):"))
    #while que no permite numeros negativos
    while(radio<=0):
        print("Solo ingrese numeros positivos")
        radio=float(input("Ingrese el radio del circulo(m):"))
    
    return radio

def calcularAreaDelCirculo(radio):
    '''
    Funcion que obtiene el area del circulo

    Parametros:
    ------------
        radio : float

    Retorna:
    ------------
        areaCirculo : float
    '''
    #resolviendo la formula para obtener el area del circulo
    areaCirculo = math.pi*(radio**2)
    #retornamos el area del circulo
    return areaCirculo

if __name__ == '__main__':
    print("Calcular el area de un circulo")
    #leemos variables
    radio=leer_variables()
    #el valor que retorne esta funcion se guarda en areaCirculo
    areaCirculo= calcularAreaDelCirculo(radio)
    #imprimo el area del circulo
    print("El area del circulo es: ",areaCirculo)