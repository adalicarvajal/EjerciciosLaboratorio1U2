def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        x : float
        y : float
    '''
    #ingreso el valor de las variables X y Y
    x=float(input("Ingrese el valor de x:"))
    y=float(input("Ingrese el valor de y:"))
    
    #retornamos la o las variables
    return x,y
def calcularPotenciaDeDosNumeros(x,y):
    '''
    Funcion que calcula la potencia de dos numeros x^y

    Parametros:
    ------------
        x : float
        y : float

    Retorna:
    ------------
        potencia : float
    '''
    #calculando la potencia
    potencia = (x**y)
    #retornamos potencia
    return potencia
if __name__ == '__main__':
    print("Hallar la potencia de cualquier numero x^y")
    #leemos variables
    x,y=leer_variables()
    #el valor que retorne esta funcion se guarda en potencia
    potencia = calcularPotenciaDeDosNumeros(x,y)
    #imprimo la potencia
    print(x," elevado a ",y," es: ", potencia)