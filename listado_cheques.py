import csv
from datetime import datetime
from datetime import date

DNIINDEX=8
TIPOINDEX=9
ESTADOINDEX=10
FECHAORIGENINDEX=6
FECHAPAGOINDEX=7

f=open("test.csv", "r") #INSERTAR ARCHIVO CSV
#f=open("archivo.csv", "r")

campos= ["NroCheque","CodigoBanco","CodigoSucursal","NumeroCuentaOrigen","NumeroCuentaDestino","Valor","FechaOrigen","FechaPago","DNI","Estado"]

datos_csv= csv.reader(f)
datos=[]
for linea in datos_csv: #Mete los datos del csv en datos[]
    datos.append(linea)



def searchDNI(dni): #BUSCA EL USUARIO INGRESANDO EL DNI Y DEVUELVE UNA LISTA CON TODOS LOS CHEQUES DEL DNI
    listadni=[]
    for usuario in datos:
        if(usuario[DNIINDEX]==dni):
            listadni.append(usuario)
    return listadni        

def csvOutput(usuario): #INGRESA LA LISTA DEL USUARIO, CREA UN ARCHIVO CSV USANDO EL FORMATO Y IMPRIME LOS DATOS DEL PRIMER CHEQUE DEL USER
    for cheques in usuario:
        listtoprint=["Fecha Origen: "+ cheques[FECHAORIGENINDEX] , " Fecha Pago: "
        +cheques[FECHAPAGOINDEX]," Valor: "+cheques[5]," Cuenta: "+cheques[3]]
        with open(cheques[DNIINDEX]+" "+str(datetime.timestamp(datetime.now()))+".csv", 'w', newline='') as output:
            writer=csv.writer(output)
            writer.writerow(listtoprint)
        pass

def csvOutput2(usuario): #INGRESA LISTA DEL USUARIO, CREA ARCHIVO CSV CON EL FORMATO E IMPRIME LOS DATOS PEDIDOS DE TODOS LOS CHEQUES
    with open(usuario[0][DNIINDEX]+" "+str(datetime.timestamp(datetime.now()))+".csv", 'a') as output:
        for cheques in usuario:
            for cheque in cheques:
                output.write(str(cheque) + ',')
            output.write('\n')

def pantallaOutput(usuario): #IMPRIME LA LISTA DEL USUARIO EN LA PANTALLA
    for cheques in usuario:
        print( "NroCheque: " +cheques[0]+" CodigoBanco: " +cheques[1]+
        " CodigoSucursal: "+cheques[2]+" NumeroCuentaOrigen: "+cheques[3]+
        " NumeroCuentaDestino: "+cheques[4]+" Valor: "+cheques[5]+
        " Fecha Origen: "+ cheques[FECHAORIGENINDEX] + " Fecha Pago: "+cheques[FECHAPAGOINDEX]+
        " Dni: " + cheques[DNIINDEX] + " Estado: "+cheques[ESTADOINDEX] + " Tipo: "+cheques[TIPOINDEX])

def estadoCheque(usuario,estado): #MODIFICA LA LISTA DE CHEQUES SEGUN EL ESTADO
    listafinal=[]
    for cheques in usuario:
        if (cheques[ESTADOINDEX]==estado):
            listafinal.append(cheques)
        elif (estado==""):
            listafinal.append(cheques)
    return listafinal

def tipoCheque(usuario,tipo): #MODIFICA LA LISTA DE CHEQUES SEGUN EL TIPO
    listafinal=[]
    for cheques in usuario:
        if (cheques[TIPOINDEX]==tipo):
            listafinal.append(cheques)
    return listafinal



def filtrarRangoFecha(usuario,desde,hasta): #PLANTILLA DE LA FUNCION PARA FILTRAR POR FECHA
    listafinal=[]
    for cheques in usuario:
        if (desde<= date.fromtimestamp(cheques[FECHAORIGENINDEX]) <= hasta):
            listafinal.append(cheques)
    return listafinal

def main(): #MAIN DEL PROGRAMA
    # f=input("Ingrese nombre de archivo csv")
    listausuario=searchDNI(str(input("Ingrese DNI sin comas ni puntos: ")))
    # print(listausuario)
    salida=input("Ingrese parametro de salida: ")
    
    #Modifica segun el tipo del cheque
    listausuario=tipoCheque(listausuario,input("Imprimir cheque por tipo:\nEMITIDO o DEPOSITADO: "))
    
    #Modifica segun el estado del cheque
    if("SI"==input("Filtrar por estado de cheque? INSERTE SI o NO: ")):
        listausuario=estadoCheque(listausuario,input("Imprimir cheque por estado:\nPENDIENTE, APROBADO, RECHAZADO: "))
    
    #Filtro de rango de fechas    
    if("SI"==input("Filtrar por rango de fecha? INSERTE SI o NO: ")):
        listausuario=filtrarRangoFecha(listausuario,date.fromtimestamp(input("Ingrese primer fecha de filtrado en timestamp:")),date.fromtimestamp(input("Ingrese fecha de cierre de filtrado en timestamp:")))
    
    if(salida=="CSV"): #IMPRIME SEGUN LA SALIDA DETERMINADA ANTERIORMENTE
        csvOutput2(listausuario)
    elif(salida=="PANTALLA"):
        pantallaOutput(listausuario)




main()
