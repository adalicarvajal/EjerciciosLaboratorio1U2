def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        libras : float
    '''
    #ingreso la cantidad de libras
    libras=float(input("Ingrese la cantidad de libras a transformar:"))
    #while que no permite numeros negativos
    while(libras<=0):
        print("No ingrese numeros negativos!")
        libras=float(input("Ingrese la cantidad de libras a transformar:"))
    return libras

def transformarLibrasAGramos(libras):
    '''
    Funcion que transforma libras a gramos

    Parametros:
    ------------
        libras : float

    Retorna:
    ------------
        gramos : float
    '''
    #transformando libras a gramos
    gramos = libras*453.6
    #retornamos gramos
    return gramos

def transformarLibrasAKilogramos(libras):
    '''
    Funcion que transforma libras a kilogramos

    Parametros:
    ------------
        libras : float

    Retorna:
    ------------
        kilogramos : float
    '''
    #transformando libras a kilogramos
    kilogramos = libras/2.205
    #retornamos kilogramos
    return kilogramos
if __name__ == '__main__':
    print("convertir libras a gramos y kilogramos")
    #leemos variables
    libras=leer_variables()
    #el valor que retorne esta funcion se guarda en gramos
    gramos= transformarLibrasAGramos(libras)
    #el valor que retorne esta funcion se guarda en kilogramos
    kilogramos= transformarLibrasAKilogramos(libras)

    #imprimo las transformaciones
    print("Libras a gramos es: ",gramos)
    print("Libras a kilogramos es: ",kilogramos)