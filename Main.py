from Funciones import * 
continuar =  True
"""""
Case 1: El nombre del archivo deberia ser ingresado por consola para darle al usuario mas libertad al momento de cargar el archivo para leer. Case
2: Buen funcionamiento. 
Case 3: Buen funcionamiento. 
Case 4: Buen funcionamiento. 
Case 5: Buen funcionamiento pero muy desprolijo. (Arreglado)
Case 6:
Mal funcionamiento al mismo tiempo, cuando se pone una marca existente como Pedigree   
mostras los 3 insumos de esa marca pero al momento de seleccionar Alimento para perros te selecciona ambos insumos, el de 12.99 y el de 19.50
y tampoco pedis la cantidad de ese insumo, y lo que guardas como ticket es solamente es una lista vacia si queda vacia la compra o una lista con
los diccionarios que representarian una compra lo cual no es del todo correcto. 
Case 7: 

Case 8: 

Case 9: 

 estan en el case 10 bajo el nombre salir del programa. 
El funcionamiento del alta de un insumo y guardarlo en un archivo csv o json deberia estar por separado y con su respectiva opcion en el menu. Dejando eso de lado, el alta
esta mal... el , , si se ingresa algun campo vacio el case genera una exception no controlada
y la parte de guardar esta totalmente mal... Luego de dar de alta un producto,  Observaciones generales: Falta desarrollar mucho codigo, falta validar mucho, falta manejar mejor el control de errores, falta distinguir mucho entre como se guarda en csv y como en json.
11- El programa deberá permitir agregar un nuevo producto a la lista (mediante una
nueva opción de menú).
Al momento de ingresar la marca del producto se deberá mostrar por pantalla un
listado con todas las marcas disponibles. Las mismas serán cargadas al programa
desde el archivo marcas.txt.
En cuanto a las características, se podrán agregar un mínimo de una y un máximo
de 3.
12. Agregar una opción para guardar todos los datos actualizados (incluyendo las altas).
El usuario elegirá el tipo de formato de exportación: csv o json.

"""


menu()

print("Finalisacion del programa")