def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        dolares : float
    '''
    #ingreso el valor en dolares
    dolares=float(input("Ingrese la cantidad en dolares:"))
    #while que no permite numeros negativos
    while(dolares<=0):
        print("No ingrese numeros negativos!")
        a=float(input("Ingrese la cantidad en dolares:"))
    #retornamos la o las variables
    return dolares

def transformarDolaresAEuros(dolares):
    '''
    Funcion que transforma dolares a euros

    Parametros:
    ------------
        dolares : float

    Retorna:
    ------------
        euros : float
    '''
    #transformando dolares a euros
    euros = 0.94*dolares
    #retornamos euros
    return euros

def transformarDolaresAYenes(dolares):
    '''
    Funcion que transforma dolares a yenes

    Parametros:
    ------------
        dolares : float

    Retorna:
    ------------
        yenes : float
    '''
    #transformando dolares a yenes
    yenes = 132.94*dolares
    #retornamos yenes
    return yenes
if __name__ == '__main__':
    print("Transformar dolares a euros y yen")
    #leemos variables
    dolares=leer_variables()
    #el valor que retorne esta funcion se guarda en euros
    euros= transformarDolaresAEuros(dolares)
    #imprimo la transformacion dolares a euros
    print("Dolares a Euros: ",euros)
    #el valor que retorne esta funcion se guarda en yenes
    yenes= transformarDolaresAYenes(dolares)
    #imprimo la transformacion dolares a yenes
    print("Dolares a yenes: ",yenes)