import send2trash
import glob
import os

def Vaciar():
    if(opc == 1):
        try:
            send2trash.send2trash(r"C:\$Recycle.Bin\S-1-5-21-2063468604-2351715026-4286032065-1001")
            print("La papelera de reciclaje se ha vaciado correctamente") 
        except Exception as e:
            print("La papelera no se ha podido vaciar :c")
        input()
        os.system('cls')

    if(opc == 2):
        global extension
        extension = input("Dame la extension del fichero incluyendo punto -> ")
        files_to_delete = glob.glob(f"C:\\$Recycle.Bin\\S-1-5-21-2063468604-2351715026-4286032065-1001\\*{extension}")
        count = 0
        if files_to_delete:
            for file in files_to_delete:
                send2trash.send2trash(file)
                count += 1
            x = int(count/2)
            print(f"Se eliminaron {x} archivos con la extensión '{extension}'.")
        else:
            print(f"No se encontraron archivos con la extensión '{extension}'.")
        input()
        os.system('cls')

opc = 0
extension = ''

def Menu():
    global opc
    while opc != 3:
        print("Elige una de las siguientes opciones")
        print("1. Vaciar la papelera completamente")
        print("2. Solo eliminar ficheros con alguna extension")
        print("3. Salir")
        opc = int(input("opc -> "))
        if(opc != 3):
            Vaciar()
        
Menu()