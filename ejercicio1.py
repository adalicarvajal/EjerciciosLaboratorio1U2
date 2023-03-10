def horasTrabajadas_por_costeHora(hTrabajadas,costoHora):
    '''
    Funcion que multiplica las horas trabajadas y el coste por hora para calcular el sueldo

    Parametros:
    ------------
        hTrabajadas : int
        costoHora : float

    Retorna:
    ------------
        sueldo : float
    '''
    #multiplicamos las horas trabajadas y el coste por hora para obtener el sueldo
    sueldo=hTrabajadas*costoHora
    #devolvemos como float a sueldo
    return sueldo

if __name__ == '__main__':
    #ingreso el numero de horas trabajadas
    hTrabajadas=int(input("Ingrese horas trabajadas:"))
    #whille que no permite ingresar numeros negativos
    while(hTrabajadas<=0):
        hTrabajadas=int(input("Ingrese horas trabajadas:"))
    #ingreso del coste por hora
    costoHora=float(input("Ingrese el coste por horas trabajadas:"))
    #whille que no permite ingresar numeros negativos
    while(costoHora<=0):
        costoHora=float(input("Ingrese el coste por horas trabajadas:"))
    #el valor que se genere en la funcion se guarda en sueldo
    sueldo=horasTrabajadas_por_costeHora(hTrabajadas,costoHora)
    #imprime el sueldo
    print("El sueldo es: ",sueldo)