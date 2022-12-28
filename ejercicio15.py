def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        cm : float
    '''
    #ingreso el valor de la variable cm
    cm=float(input("Ingrese la cantidad de centimetros:"))
    while(cm<=0):
        print("No ingrese numeros negativos!")
        cm=float(input("Ingrese la cantidad de centimetros:"))

    #retornamos la o las variables
    return cm

def transformarCentimetrosAMetros(cm):
    '''
    Funcion que transforma centimetos a metros

    Parametros:
    ------------
        cm : float

    Retorna:
    ------------
        metros : float
    '''
    #transformando cm a metros
    metros = cm/100
    #retornamos metros
    return metros

def transformarCentimetrosAKilometros(cm):
    '''
    Funcion que transforma centimetos a kilometros

    Parametros:
    ------------
        cm : float

    Retorna:
    ------------
        kilometros : float
    '''
    #transformando cm a kilometros
    kilometros = cm/100000
    #retornamos kilometros
    return kilometros
if __name__ == '__main__':
    print("convertir centimetros a metros y kilometros")
    #leemos variables
    cm=leer_variables()
    #el valor que retorne esta funcion se guarda en metros
    metros= transformarCentimetrosAMetros(cm)
    #el valor que retorne esta funcion se guarda en kilometros
    kilometros=transformarCentimetrosAKilometros(cm)
    
    #imprimo las transformaciones
    print(cm," centimetro(s) son ",metros," metro(s)")
    print(cm," centimetro(s) son ",kilometros," kilometro(s)")