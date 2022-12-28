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
        altura : float
    '''
    #ingreso el radio del cilindro
    radio=float(input("Ingrese el radio del cilindro(cm):"))
    #while que no permite numeros negativos
    while(radio<=0):
        print("Solo ingrese numeros positivos")
        radio=float(input("Ingrese el radio del cilindro(cm):"))
    #ingreso la altura del cilindro
    altura=float(input("Ingrese la altura del cilindro(cm):"))
    #while que no permite numeros negativos
    while(altura<=0):
        print("Solo ingrese numeros positivos")
        altura=float(input("Ingrese la altura del cilindro(cm):"))

    return (radio,altura)

def calcularAreaDelCilindro(radio,altura):
    '''
    Funcion que obtiene el area de un cilindro

    Parametros:
    ------------
        radio : float
        altura : float

    Retorna:
    ------------
        areaCilindro : float
    '''
    #resolviendo la formula para obtener el area del cilindro
    areaCilindro = (radio+altura)*(2*math.pi*radio)
    #retornamos el area del cilindro
    return areaCilindro

if __name__ == '__main__':
    print("Calcular el area de un cilindro")
    #leemos variables
    radio,altura=leer_variables()
    #el valor que retorne esta funcion se guarda en areaCilindro
    areaCilindro= calcularAreaDelCilindro(radio,altura)
    #imprimo el area del cilindro
    print("El area del cilindro es: ",areaCilindro)