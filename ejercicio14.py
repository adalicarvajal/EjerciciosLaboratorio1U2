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
    #ingreso el valor de la variable a y b
    a=float(input("Ingrese el valor de la variable a:"))
    b=float(input("Ingrese el valor de la variable b:"))
    #retornamos la o las variables
    return a,b

def sumarVariables(a,b):
    '''
    Funcion que suma dos variables

    Parametros:
    ------------
        a : float
        b : float

    Retorna:
    ------------
        suma : float
    '''
    #sumando las dos variables
    suma = a+b
    #retornamos suma
    return suma

def restarVariables(a,b):
    '''
    Funcion que resta dos variables

    Parametros:
    ------------
        a : float
        b : float

    Retorna:
    ------------
        resta : float
    '''
    #sumando las dos variables
    resta = a-b
    #retornamos resta
    return resta

def multiplicarVariables(a,b):
    '''
    Funcion que multiplica dos variables

    Parametros:
    ------------
        a : float
        b : float

    Retorna:
    ------------
        multiplicacion : float
    '''
    #multiplicando las dos variables
    multiplicacion = a*b
    #retornamos multiplicacion
    return multiplicacion

def dividirVariables(a,b):
    '''
    Funcion que divide dos variables

    Parametros:
    ------------
        a : float
        b : float

    Retorna:
    ------------
        division : float
    '''
    #dividiendo las dos variables
    division = a/b
    #retornamos division
    return division
if __name__ == '__main__':
    print("Ingresar dos numeros y realizar todas las operaciones aritmeticas")
    #leemos variables
    a,b=leer_variables()
    #el valor que retorne esta funcion se guarda en suma
    suma= sumarVariables(a,b)
    #el valor que retorne esta funcion se guarda en resta
    resta= restarVariables(a,b)
    #el valor que retorne esta funcion se guarda en multiplicacion
    multiplicacion= multiplicarVariables(a,b)
    #el valor que retorne esta funcion se guarda en division
    division= dividirVariables(a,b)
    #imprimo la suma,resta,multiplicacion y division
    print("Suma de ",a,"+",b,":",suma)
    print("Resta de ",a,"-",b,":",resta)
    print("Multiplicacion de ",a,"*",b,":",multiplicacion)
    print("Division de ",a,"/",b,":",division)
