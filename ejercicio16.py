def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        distancia : float
        tiempo : float
    '''
    #ingreso el valor de la distancia y tiempo
    distancia=float(input("Ingrese la distancia(metros):"))
    while(distancia<=0):
        print("No ingrese numeros negativos!")
        distancia=float(input("Ingrese la distancia(metros):"))
    tiempo=float(input("Ingrese el tiempo(segundos):"))
    while(tiempo<=0):
        print("No ingrese numeros negativos!")
        distancia=float(input("Ingrese el tiempo(segundos):"))
    #retornamos la o las variables
    return distancia,tiempo

def calcularVelocidad(distancia,tiempo):
    '''
    Funcion que calcula la velocidad con la formula v=d/t

    Parametros:
    ------------
        distancia : float
        tiempo : float

    Retorna:
    ------------
        velocidad : float
    '''
    #calculando la velocidad
    velocidad = distancia/tiempo
    #retornamos velocidad
    return velocidad

if __name__ == '__main__':
    print("Calcular la formula de la velocidad v=d/t")
    #leemos variables
    distancia,tiempo=leer_variables()
    #el valor que retorne esta funcion se guarda en velocidad
    velocidad = calcularVelocidad(distancia,tiempo)
    
    #imprimo la velocidad
    print("v=d/t es igual a: ",velocidad, "m/s")
