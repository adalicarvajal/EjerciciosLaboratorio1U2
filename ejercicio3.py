def leer_variables():
    '''
    Funcion que lee n variables

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        largo : float
        ancho : float
    '''
    #ingreso el largo del rectangulo
    largo=float(input("Ingrese el largo del rectangulo(cm):"))
    #whille que no permite ingresar numeros negativos
    while(largo<=0):
        print("Ingrese numeros positivos!")
        inversion=float(input("Ingrese el largo del rectangulo(cm):"))

    #ingreso el ancho del rectangulo
    ancho=float(input("Ingrese el ancho del rectangulo(cm):"))
    #whille que no permite ingresar numeros negativos
    while(ancho<=0):
        print("Ingrese numeros positivos!")
        ancho=float(input("Ingrese el ancho del rectangulo(cm):"))
    return (largo,ancho)
def calcularAreaDeUnRectangulo(largo,ancho):
    '''
    Funcion que obtiene el area de un rectangulo

    Parametros:
    ------------
        largo : float
        ancho : float

    Retorna:
    ------------
        area : float
    '''
    #calculando area
    area=largo*ancho
    #retorno area
    return area

def calcularPerimetroDeUnRectangulo(largo,ancho):
    '''
    Funcion que obtiene perimetro de un rectangulo

    Parametros:
    ------------
        largo : float
        ancho : float

    Retorna:
    ------------
        perimetro : float
    '''
    #calculando perimetro
    perimetro=(largo*2)+(ancho*2)
    #retorno perimetro
    return perimetro

if __name__ == '__main__':
    print("Area y perimetro de un rectangulo")
    #leemos variables
    largo,ancho=leer_variables()
    #el valor que retorne esta funcion se guarda en area
    area=calcularAreaDeUnRectangulo(largo,ancho)
    #imprimo area del rectangulo
    print("El area del rectangulo es: ",area)
    #el valor que retorne esta funcion se guarda en area
    perimetro= calcularPerimetroDeUnRectangulo(largo,ancho)
    #imprimo perimetro del rectangulo
    print("El perimetro del rectangulo es: ",perimetro)
