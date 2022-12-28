def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        nombre : str
    '''
    #ingreso el valor de las variables a y b
    nombre=input("Ingrese su nombre:")
    return nombre

if __name__ == '__main__':
    #leer nombre
    nombre=leer_variables()
    print("Hola, como estas ",nombre,"?")