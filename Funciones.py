import os
import re
import json
import csv
import random
# Esta funcion pasa los datos del csv a una lista
def Cargar_csv(path:str)->list:
    lista = []
    with open(path,encoding='utf-8') as file:
        
        for linea in file:

            lista.append(linea.strip().split(","))
    return lista

def Numero_random():
    cantidad_stock = random.randrange(0,10)
    

    return cantidad_stock

def es_Un_numero(numero:str)->bool:
    try:
        int(numero)
        return False
    except ValueError:
        return True

def cambiar_nombre_csv(archivo:str,nombre_nuevo:str)->None:
    if archivo.endswith(".csv"):
        try:
            a = os.rename(archivo, nombre_nuevo + ".csv")
        except Exception as fallo:
            print("Hubo un error al renombrar el csv",str(fallo))
    else:
        print("No es un archivo csv")

#Esta funcion transfomra una lista en un diccionario
def Pasar_a_dict(lista_dict:list)->dict:
    lista_return = []

   
    
    for item in lista_dict:
        stock_disponible = Numero_random()

        lista_return.append({'ID':item[0],'nombre':item[1],'marca':item[2],'precio':item[3],'caracteristicas':item[4],'stock':stock_disponible})
    
    return lista_return

#Esta funcion printeas el diccionario discriminando ciertos elementos
def Mostrar_insumos(lista:list,dicionario:dict, key:str)->None:
    for i in lista:
        for d in dicionario:
            if i == d[key]:
                print(d)

#Esta funcion elimina las repeticiones de una lista
def Sacar_repetidos(List:list)->list:
    conjunto = set(List)
    return conjunto

#Esta funcion aisla la marca que se requirio para asi posteriormente mostrar los productos
def Separar_mostrar_productos(dict:dict,list:set)->None:
    for marca in list:
        print("Marcas :" + marca)
        for producto in dict:
            if(producto['marca'] == marca):
                print(producto['marca'], producto['nombre'])
        print("----------------------------------------------------------")

#Esta funcion muestra los productos y el precio de una marca
def Separara_marca_precio(diccionario:dict,lista:set)->None:
    for marca in lista:
        print("Marcas :" + marca)
        for producto in diccionario:
            if(producto['marca'] == marca):
                print(producto['marca'], producto['nombre'], producto['precio'])
        print("----------------------------------------------------------")

#Esta funcion discrimina un diccionario por los nombres
def Separar_Por_nombres(diccionario:dict,lista:list)->dict:
    listaJson = []
    for Nombre in lista:
        for producto in diccionario:
            
            if Nombre == producto['nombre']:
                listaJson.append({producto['ID'],producto['nombre'],producto['marca'],producto['precio']})
        print("----------------------------------------------------------")
    return listaJson

#Esta funcion agrupa a los elementos de una misma marca en un diccionario
def Separar_marca(dict: dict, key:str)-> list:
    lista = []
    for nombre in dict:
        lista.append(nombre[key])
    conjunto = set(lista)
    return conjunto

#Esta funcion busca parecidos en las caracteristicas y devuelve en una lista los nombres de los elementos con coincidencias
def Buscar_insumo(dict: dict, key:str,key2)->list:
    lista = []
    caracteristica = re.compile(key)
    for item in dict:
        Similitud = caracteristica.search(item[key2])
        if Similitud:
            lista.append(item['nombre'])
        else:
            pass
    return lista

#Esta funcion busca parecidos en las caracteristicas y devuelve en una lista todo el diccionario de los elementos con coincidencias
def Buscar_insumo2(dict: dict, key:str,key2:str)->dict:
    lista = []
    caracteristica = re.compile(key)
    for item in dict:
        Similitud = caracteristica.search(item[key2])
        if Similitud:
            lista.append({'ID':item['ID']
                          ,'nombre':item['nombre']
                          ,'marca':item['marca']
                          ,'precio':item['precio']
                          ,'caracteristicas':item['caracteristicas']})
        else:
            pass
    lista1 = (lista)
    return lista1


#Esta funcion ordena alfabeticamente un diccionario
def Ordenar_alfabeticamente(lista:list)->list:
    Marca_ordenada = sorted(lista)
    return Marca_ordenada

#Esta funcion Crea un diccionario que ordena ascendentemente los precios
def Crear_diccionario_ordenado(lista:list,dict:dict)->dict:
    diccionario_ordenado = []
    id_anterior = []
    marca_anterior = None
    for marca in lista:
        for id in dict:
            if marca_anterior == id['marca']:
                if precio_anterior > id['precio']:
                    diccionario_ordenado.append(id)
                elif precio_anterior < id['precio']:
                    diccionario_ordenado.append(id_anterior)
            if id['marca'] == marca:
                marca_anterior= id['marca']
                precio_anterior = id['precio']
                id_anterior = id
                diccionario_ordenado.append(id_anterior)
    return diccionario_ordenado

#Esta funcion almacena el valor de los productos seleccionados para devolverlos en una lista
def Comprar_productos(diccionario:dict,key:str)->list:
    lista = []
    lista_true = []
    verifica_marca = True
    flag_no_existe = True
    flag_cantidad = True
    contador = 0
   
    while verifica_marca:
        flag_no_existe = True
        
        for marca in diccionario:
            if marca['marca'] == key:
                contador += 1
                print(marca['nombre'],marca['precio'])
                verifica_marca = False
                flag_no_existe = False
        if contador == 0 and flag_no_existe:
                print("esa marca no existe coloque una que existe")
                key = input("Ingrese una marca de la lista")

    compra = input("Que producto desea comprar: ")
    while compra == "":
        compra = input("usted no esta comprando nada, coloque lo que quiere comprar")

    cantidad = (input("Cuantos ejemplares de este producto quiere: "))
    while es_Un_numero(cantidad):
        print("Lo que agregaste no es un numero")
        cantidad = input("Ingrese el numro de caracteristicas: ")
    
    while cantidad == "0":
        cantidad = input("la cantidad no puede ser 0 tiene que ser 1 o mas")
    cantidad = int(cantidad)
    while flag_cantidad:
        for item in diccionario:

            if compra == item['nombre'] and item['marca'] == key and cantidad <= item['stock']:
                flag_cantidad = False

        if flag_cantidad:
            print("La cantidad no puede ser mayor al stock disponible")
            cantidad = (input("Ingrese la cantidad que quiere siendo igual o menor a la cantidad de stock"))
            if es_Un_numero(cantidad):
                print("esto no es un numero")
            else:
                cantidad = int(cantidad)

    
    for item in diccionario:
        if compra == item['nombre'] and item['marca'] == key:
            print(item['nombre'],item['precio'])
            lista.append({"cantidad":cantidad,"nombre" :item['nombre'],"precio":item['precio']})
    if contador > 1:
        print("elija uno solo de los productos ")
        print("Hay 1 0 mas productos repetidos: ")
        for i in lista:
            print(i)
        print("-----------------------------")
        print("elija uno solo de los productos ")
        for i in lista:
            print(i)
            eleccion = "no"
            eleccion = input("queres este prodcuto")
            if eleccion == "si":
                lista_true.append(i)
    else:
        for item in lista:
            lista_true.append({"cantidad":cantidad,"nombre" :item['nombre'],"precio":item['precio']})
        
    return lista_true

#Esta funcion suma los precios de una lista
def Sumar_precio(lista:list)->float:
    precio = 0
    for i in list:
        Pagar = float(i['precio'])
        precio+=Pagar
    return precio

#Esta funcion esta funcion pasa una lista a un arrays de strings
def Pasar_a_string(lista:list)->list:
    lista = []
    for palabra in lista:
      lista.append(str(palabra))
    lista_strings = str(lista)
    return lista_strings

#Esta funcion agrega un aumento porcentual al precio del diccionario
def Aumento_precio(diccionario:dict)->dict:
        lista = []
        precio_str = diccionario['precio'].replace("$","")
        precio = float(precio_str)
        precio_aumentado = precio*1.084
        diccionario['precio'] = precio_aumentado

        return diccionario

def Agregar_insumos(diccionario:dict)->dict:
    lista = []
    lista_marcas = []
    seguir = True
        
    id = len(diccionario)+1
    nombre = input("ingrese el nombre del producto: ")
    while nombre == "":
        print("el campo esta vacio:")
        nombre = input("Ingrese el nombre del producto: ")
    with open("Primer_Parcial\marcas.txt",encoding='utf-8') as file:
           
        for i in file:
            lista_marcas.append(i)
            print("-------------------------------------------------------")
            print("                  ",i,"                  ")
        
    while seguir:
        marca_1 = input("ingrese la marca del producto: ")
        marca = (marca_1+"\n")
        print(marca)
        for i in lista_marcas:
                
            if i == marca:
                seguir = False
                break
        if seguir:
            print("esa marca no esta registrada, ingrese otra")
                
            
    precio = input("Ingrese el precio del producto: ")
    while es_Un_numero(precio):
        print("Lo que agregaste no es un numero")
        precio = input("Ingrese el precio del producto: ")

    cantidad = (input("Cuantas caracteristicas desea agregar al producto: "))
    while es_Un_numero(cantidad):
        print("Lo que agregaste no es un numero")
        cantidad = input("Ingrese el numro de caracteristicas: ")
    
    cantidad = int(cantidad)

    
    

    match cantidad:
        case 1:
            carac_1 = input("Ingrese la caracteristica: ")
            while carac_1 == "":
                carac_1 = input("El campo esta vacio escriba la caracteristica")
        case 2:
            carac_1 = input("Ingrese la primer caracteristica: ")
            while carac_1 == "":
                carac_1 = input("El campo esta vacio escriba la primer caracteristica: ")
            carac_2 = input("Ingrese la segunda caracteristica: ")
            while carac_2 == "":
                carac_2 = input("El campo esta vacio escriba la segunda caracteristica: ")
        case 3:
            carac_1 = input("Ingrese la primer caracteristica: ")
            while carac_1 == "":
                carac_1 = input("El campo esta vacio escriba la primer caracteristica: ")
            carac_2 = input("Ingrese la segunda caracteristica: ")
            while carac_2 == "":
                carac_2 = input("El campo esta vacio escriba la segunda caracteristica: ")
            carac_3 = input("Ingrese la tercer caracteristica: ")
            while carac_3 == "":
                carac_3 = input("El campo esta vacio escriba la tercer caracteristica: ")
        
    match cantidad:
        case 1:
            diccionario.append({'ID':id,'nombre':nombre,'marca':marca_1,'precio':precio,'caracteristicas':carac_1})
        case 2:
            diccionario.append({'ID':id,'nombre':nombre,'marca':marca_1,'precio':precio,'caracteristicas':carac_1+ " " + carac_2})
        case 3:
            diccionario.append({'ID':id,'nombre':nombre,'marca':marca_1,'precio':precio,'caracteristicas':carac_1+ " "+ carac_2+ " "+ carac_3})

    print(diccionario)
    return diccionario

def pasar_a_csv(diccionario:dict)->list:
    lista = []
    for i in diccionario:
        aux = str(i['ID'])
        lista.append({""+ aux +""+ i['nombre']+""+i['marca']+""+i['precio']+""+i['caracteristicas']}) 
    return lista


def Mostrar_Stock_marca(diccionario:dict,key:str):
    for item in diccionario:
        if item['marca'] == key:
            aux =  str(item['stock'])
            print("Nombre producto:"+ item['nombre']+ "--precio producto: "+ item['precio']+"--stock producto: "+ aux)

def Mostrar_insumos_menor_que(diccionario:dict,numero_menor:int)->list:
    numero_menor = int(numero_menor)
    lista = []
    for item in diccionario:
        aux = int(item['stock'])
        if aux <= numero_menor:
            aux = str(item['stock'])
            lista.append({" "+item['nombre']+" "+aux})

    return lista


def menu():
        a = True
        bandera_Cargar_Datos = True
        bandera_json = True
        lista = []
        Comprado = []
        while True:
            a = input("Pulsa enter para mostrar el menu:")
            seguir = "si"
            os.system("cls")
            print(""" 
            **** Menu de opciones ***
                1-Cargar datos
                2-Listar cantidad de marcas
                3-Limiar insumos por marca
                4-Buscar insumos por caracteristicas
                5-Listar insumos ordenados
                6-Realizar compras
                7-Formar en formato JSON
                8-Leer desde el formato JSON
                9-Actualizar precios
                10-Agregar producto a la lista
                11-Guardar los prodcutos agregados en json o csv
                12-Mostrar cantidad de stock por marca
                13-Imprimir porductos con 2 0 mas unidades de stock
                14- salir del programa
            """)
            Numero = input("Ingrese una opcion ")
            if es_Un_numero(Numero):
                print("Eso no es un numero")
            else:
                Numero = int(Numero)
                match(Numero):
                    case 1:
                        #Primer_Parcial\Insumos.csv
                        a = input("Ingrese el .csv que debe ser leido: ")
                        print(a)
                        lista = Cargar_csv(a)
                        diccionario = Pasar_a_dict(lista)
                        for i in diccionario:
                            print(i)
                        bandera_Cargar_Datos = False
                    case 2:
                        if bandera_Cargar_Datos == True:
                            print("Cargue los datos Por favor")
                        else:
                            conjunto = Separar_marca(diccionario, 'marca')
                            Separar_mostrar_productos(diccionario,conjunto)
                    case 3:
                        if bandera_Cargar_Datos == True:
                            print("Cargue los datos Por favor")
                        else:
                            conjunto = Separar_marca(diccionario, 'marca')
                            Separara_marca_precio(diccionario,conjunto)
                    case 4:
                        if bandera_Cargar_Datos == True:
                            print("Cargue los datos Por favor")
                        else:
                            carac = input("Ingrese la caracteristica que desee en el producto: ")
                            Lista_caracteristicas_buscada = Buscar_insumo(diccionario,carac,'caracteristicas')
                            Mostrar_insumos(Lista_caracteristicas_buscada,diccionario,'nombre')
                    case 5:
                        if bandera_Cargar_Datos == True:
                            print("Cargue los datos Por favor")
                        else:
                            conjunto = Separar_marca(diccionario, 'marca')
                            Alfabetico = Ordenar_alfabeticamente(conjunto)
                            Diccionario_ordenado= Crear_diccionario_ordenado(Alfabetico,diccionario)
                            for i in Diccionario_ordenado:
                                print(i)
                        
                    case 6:
                        acumulador = 0
                        if bandera_Cargar_Datos == True:
                            print("Cargue los datos Por favor")
                        else:
                            while seguir == "si":
                                for i in diccionario:
                                    print(i['marca'])
                                compra = input("Ingrese la marca de la cual se quiere comprar podructos: ")
                                while compra == "":
                                    compra = input("La marca no puede ser un campo vacio")
                                comprando = Comprar_productos(diccionario, compra)
                                for item in comprando:
                                    print(item['precio'])
                                    if item['precio'] == "$9.99":
                                        a = 10
                                    else:
                                        m =re.findall(r'\d+\d+',item['precio'])
                                        aux = int(m[1])
                                        aux_1 = int(m[0])
                                        if aux >= 50:
                                            a = aux_1+1
                                
                                    a = int(a)
                                    b = int(item['cantidad'])
                                    cuenta = b*a
                                    acumulador += cuenta
                                    
                                    print(acumulador)
                                print(compra)
                                if comprando == None:
                                    print("Usted no esta comprando nada ")  
                                    seguir = input("quiere comprar algo: ")
                                else:
                                    Comprado.append(comprando)
                                    seguir = input("Desea seguir comprando: ")
                            acumulador = str(acumulador)
                            Comprado.append("El total de la compra es: " + acumulador)
                            if Comprado == []:
                                    print("Useted no compro nada la lista esta vacia ")
                            else:
                                file = open(r"C:\Users\Aaron\OneDrive\Escritorio\Primer parcial real\Primer_Parcial\Compra.txt","a",encoding='utf-8')
                                file.write("\nNuevo recibo:")
                                archivo_compra = json.dumps(Comprado)
                                file.write(archivo_compra)
                                file.close
                                file = open(r"C:\Users\Aaron\OneDrive\Escritorio\Primer parcial real\Primer_Parcial\Compra.txt","r",encoding='utf-8')
                                for linea in file:
                                    print(linea)
                    case 7:
                        if bandera_Cargar_Datos == True:
                            print("Cargue los datos Por favor")
                        else:
                        
            
                            with open(r"C:\Users\Aaron\OneDrive\Escritorio\Primer parcial real\Primer_Parcial\,alimentoarchivo.json","w",encoding="utf-8") as json_file:
                                Lista_Json = Buscar_insumo2(diccionario,'Alimento','nombre')

                                producto_json = json.dumps(Lista_Json)
                                aux = str(producto_json)
                                diccionario_json= json.loads(aux)
        
                    
                                json.dump(diccionario_json,json_file,indent=4, separators=(",",":"),ensure_ascii=False)
                                bandera_json = False

                            
                    case 8:
                        if bandera_Cargar_Datos == True:
                            print("Cargue los datos Por favor")
                        elif bandera_json == True:
                            print("Cargue el documento Json")
                        else:
                            with open("Primer_Parcial\,alimentoarchivo.json","r",buffering=-1,encoding='utf-8') as json_file:
                                for linea in json_file:
                                    a = str(linea)
                                    print(a)
                            pass
                        
                    case 9:
                        if bandera_Cargar_Datos == True:
                            print("Cargue los datos Por favor")
                        else:
                            Lista_aumento = list(map(Aumento_precio,diccionario))
                            for elemento in Lista_aumento:
                                print(elemento)
                            with open(r"C:\Users\Aaron\OneDrive\Escritorio\Primer parcial real\Primer_Parcial\Pruebas.csv", "w", newline="",encoding='utf-8') as archivo_csv:
                                escribir = csv.writer(archivo_csv)
                                escribir.writerow(['ID','nombre','marca','precio','caracteristica'])

                                for i in Lista_aumento:
                                        a = str(i['precio'])
                                        archivo_csv.write(i['ID'],)
                                        archivo_csv.write(i['nombre'])
                                        archivo_csv.write(i['marca'])
                                        archivo_csv.write(a)
                                        archivo_csv.write(i['caracteristicas'])
                                        archivo_csv.write("print \n")
                    case 10:
                        if bandera_Cargar_Datos == True:
                            print("Cargue los datos Por favor")
                        else:

                            diccionario_agregado= Agregar_insumos(diccionario)
                            continuar = input("desea seguir agregando insumos")
                            while continuar == "si":
                                diccionario_agregado = Agregar_insumos(diccionario_agregado)
                                for item in diccionario_agregado:
                                    print(item)
                                    print("\n")
                                continuar = input("desea seguir agregando insumos: ")
                            
                    case 11:

                        opcion = input("Deseas el archivo en formato csv(csv = 1) o json (json = 2)")
                        if opcion == "1":
                            lista_csv = pasar_a_csv(diccionario_agregado)

                            with open("Primer_Parcial\Productos_agregados.csv","w",buffering=1,encoding='utf-8') as file:
                                for i in lista_csv:
                                    a = str(i)
                                    a = a.replace("{","")
                                    a = a.replace("}","")
                                    a = a.replace("'","")
                                    b = a+"\n"
                                    file.write(b)
                        elif opcion == "2":
                            with open("Primer_Parcial\Productos_agregados.json","w",buffering=1,encoding='utf-8') as json_file:
                                json.dump(diccionario_agregado,json_file,indent=4,separators=(",",":"),ensure_ascii=False)
                        else:
                            print("No existe esa opcion")

                    case 12:
                        flag_marca_existe = True
                        conjunto = Separar_marca(diccionario, 'marca')
                        for i in conjunto:
                            print(i)
                        marca_stock = input("Ingrese el nombre de la marca la cual quieres ver el stock")
                        while flag_marca_existe:
                            for i in conjunto:
                                if marca_stock == i:
                                    flag_marca_existe = False
                            if flag_marca_existe:
                                marca_stock = input("Ingrese una marca que exista")
                        Mostrar_Stock_marca(diccionario,marca_stock)
                        
                    case 13:
                        lista_insumos_bajos = Mostrar_insumos_menor_que(diccionario,2)
                        for i in lista_insumos_bajos:
                            print(i)
                        

                        with open("Primer_Parcial\Stock_menor_que_3.csv","w",buffering=1,encoding='utf-8') as file:
                            for i in lista_insumos_bajos:
                                a = str(i)
                                a = a.replace("{","")
                                a = a.replace("}","")
                                a = a.replace("'","")
                                b = a+"\n"
                                file.write(b)
                    case 14:
                        break
                        
