import csv
import pandas as pd

#********************************************************************Funcion Ver inventario****************************************************************************      
def VerInventario():
    df=pd.read_csv(r'inventario.csv',encoding='latin-1')
    print(df)
    menu()

#********************************************************************Funcion Buscar Nombre****************************************************************************      
def BuscarPorNombreSrv():
    df=pd.read_csv(r'inventario.csv',encoding='latin-1')
    palabra=str(input('Ingrese nombre del Servidor: '))
    if len(df[df['hostname'].str.contains(palabra)]) <= 0:
     print("No se encuentra la opcion buscada")
     pregunta = input("Si Quieres realizar otra busqueda presiona [S] sino cualquier tecla para volver al menu principal  ").upper()
     if pregunta == "S":
        BuscarPorNombreSrv()
     else:
      menu()
    else:
     print(df[df['hostname'].str.contains(palabra)])
     pregunta = input("Si Quieres realizar otra busqueda presiona [S] sino cualquier tecla para volver al menu principal  ").upper()
     if pregunta == "S":
        BuscarPorNombreSrv()
     else:
      menu()    


#********************************************************************Funcion  Buscar por IP****************************************************************************  
def BuscarPorIpSrv():
    df=pd.read_csv(r'inventario.csv',encoding='latin-1')
    palabra=str(input('Ingrese Direccion IP: '))
    if len(df[df['ip'].str.contains(palabra)]) <= 0:
     print("Esa no es una opción válida")
     pregunta = input("Si Quieres realizar otra busqueda presiona [S] sino cualquier tecla para volver al menu principal  ").upper()
     if pregunta == "S":
        BuscarPorIpSrv()
     else:
      menu()
    else:
     print(df[df['ip'].str.contains(palabra)])
     pregunta = input("Si Quieres realizar otra busqueda presiona [S] sino cualquier tecla para volver al menu principal  ").upper()
     if pregunta == "S":
        BuscarPorIpSrv()
     else:
      menu()        

#********************************************************************Funcion  Buscar por Edificio*****************************************************************************  
def BuscarPorEdificio():
    df=pd.read_csv(r'inventario.csv',encoding='latin-1')
    palabra=str(input('Ingrese el Edificio: '))
    if len(df[df['edificio'].str.contains(palabra)]) <= 0:
     print("Esa no es una opción válida")
     pregunta = input("Si Quieres realizar otra busqueda presiona [S] sino cualquier tecla para volver al menu principal  ").upper()
     if pregunta == "S":
        BuscarPorEdificio()  
     else:
      menu()
    else:
     print(df[df['edificio'].str.contains(palabra)])
     pregunta = input("Si Quieres realizar otra busqueda presiona [S] sino cualquier tecla para volver al menu principal  ").upper()
     if pregunta == "S":
        BuscarPorEdificio()  
     else:
      menu() 


 #*******************************************************************Funcion Existe Srv**********************************************************************   
def ExisteSrv(palabra):
    with open(r'inventario.csv',encoding='latin-1') as File:
        reader=csv.DictReader(File)
        for row in reader:
            if(palabra==row['hostname']):
                return row
        return "No existe"        

 #*******************************************************************Funcion Ingresa SRV**********************************************************************   
def IngresarSrv():
    nombresrv=input('Ingrese el nombre del servidor: ')
    if ExisteSrv(nombresrv)=="No existe":
        dirip=str(input('Ingrese direccion IP:'))
        edificio=str(input('Edificio:'))
        write_csv(nombresrv,dirip,edificio)
    else:
        print('ERROR: El servidor ya existe en la Base de Datos')
#*******************************************************************Funcion Escribe SRV**********************************************************************   
def write_csv(nombresrv,dirip,edificio):
    # Abrir archivo para escritura
    csvfile = open(r'inventario.csv', 'a+', newline='')

    # Detallar los nombres de las columnas
    # header = ['hostname', 'ip', 'edificio']
    datos= {'hostname': nombresrv, 'ip': dirip, 'edificio': edificio}
    # Crear el objeto para escribir las lineas de archivo
    # basado en los nombres de las columnas
    writer = csv.DictWriter(csvfile, datos)

    writer.writerow (datos)
    print("Registro exitoso")
    csvfile.close()
    pregunta = input("Si Quieres agregar otro servidor presiona [S] sino cualquier tecla para volver al menu principal  ").upper()
    if pregunta == "S":
        IngresarSrv()  
    else:
      menu()
#*******************************************************************Funcion Menu********************************************************************************
def menu():
    print("******MENU INVENTARIO******")
    print("1 - Buscar por nombre de servidor:")
    print("2 - Buscar por Direcion IP:")
    print("3 - Buscar por Edificio:")
    print("4 - Listar base de servidores:")
    print("5 - Agregar Servidor:")
    print("6 - Salir")
    opcion = int(input('Introduzca el número de la opción deseada: '))
   
    if opcion == 1:
        BuscarPorNombreSrv()
    elif opcion == 2:
        BuscarPorIpSrv()
    elif opcion == 3:
        BuscarPorEdificio()
    elif opcion == 4:
        VerInventario()    
    elif opcion == 5:
        IngresarSrv()    
        return
#*****************************************************************************************************
if __name__ == '__main__':
    
  menu()
