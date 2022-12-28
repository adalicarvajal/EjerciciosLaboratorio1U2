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
    '''
    #ingreso el valor de la variable a
    a=float(input("Ingrese el valor de la variable a:"))
    
    #ingreso el valor de la variable b
    b=float(input("Ingrese el valor de la variable b:"))
    return (a,b)

def calcularTeoremaPitagoras(a,b):
    '''
    Funcion que obtiene el teorema de pitagoras

    Parametros:
    ------------
        a : float
        b : float

    Retorna:
    ------------
        teoremaPitagoras : float
    '''
    #resolviendo la formula para obtener el teorema de pitagoras
    teoremaPitagoras = math.sqrt((a**2)+(b**2))
    #retornamos el teorema de pitagoras
    return teoremaPitagoras

if __name__ == '__main__':
    print("Calcular el teorema de pitagoras c^2= a^2 + b^2")
    #leemos variables
    a,b=leer_variables()
    #el valor que retorne esta funcion se guarda en teoremaPitagoras
    teoremaPitagoras= calcularTeoremaPitagoras(a,b)
    #imprimo el teorema de pitagoras
    print("C^2 =a^2+b^2 es: ",teoremaPitagoras)