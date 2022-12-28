def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        base : float
        altura : float
    '''
    #ingreso el valor de la base y altura de un triangulo
    base=float(input("Ingrese la base del triangulo(metros):"))
    #while que no permite numeros negativos
    while(base<=0):
        print("No ingrese numeros negativos!")
        base=float(input("Ingrese la base del triangulo(metros):"))
    altura=float(input("Ingrese la altura del triangulo(metros):"))
    #while que no permite numeros negativos
    while(altura<=0):
        print("No ingrese numeros negativos!")
        altura=float(input("Ingrese la altura del triangulo(metros):"))
    
    #retornamos la o las variables
    return base,altura
def calcularAreaDeUnTriangulo(x,y):
    '''
    Funcion que calcula el area de un triangulo

    Parametros:
    ------------
        base : float
        altura : float

    Retorna:
    ------------
        areaTriangulo : float
    '''
    #calculando el area del triangulo
    areaTriangulo = (base*altura)/2
    #retornamos el area
    return areaTriangulo
if __name__ == '__main__':
    print("Hallar el area de un triangulo")
    #leemos variables
    base,altura=leer_variables()
    #el valor que retorne esta funcion se guarda en potencia
    areaTriangulo = calcularAreaDeUnTriangulo(base,altura)
    #imprimo el area
    print("El area del triangulo es: ",areaTriangulo)