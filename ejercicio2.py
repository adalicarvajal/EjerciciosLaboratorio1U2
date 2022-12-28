def calcularCapitalObtenido(inversion,interes,años):
    '''
    Funcion que permite calcular el capital obtenido en la inversión cada año que dura la inversión.

    Parametros:
    ------------
        inversion : float
        interes : float
        años : float

    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato
    '''
    #calculando capital
    for i in range(años):
        inversion = inversion*(1 + interes / 100 )
        #imprime el capital obtenido por año
        print("Capital tras ", i+1," años: ", round(inversion, 2))


if __name__ == '__main__':
    #ingreso el monto de la inversion
    inversion=float(input("Cantidad a invertir $?:"))
    #whille que no permite ingresar numeros negativos
    while(inversion<=0):
        print("Ingrese numeros positivos!")
        inversion=float(input("Cantidad a invertir $?:"))
    #ingreso del interes
    interes=float(input("Cual es el interes porcentual anual?:"))
    #whille que no permite ingresar numeros negativos
    while(interes<=0):
        print("Ingrese numeros positivos!")
        interes=int(input("Cual es el interes porcentual anual?:"))
    #ingreso dle numero de años
    años=int(input("Ingrese el numero de años:"))
    #whille que no permite ingresar numeros negativos
    while(años<=0):
        print("Ingrese numeros positivos!")
        interes=int(input("Ingrese el numero de años:"))
    #llamada a la funcion para calcular el capital obtenido
    calcularCapitalObtenido(interes,inversion,años)
