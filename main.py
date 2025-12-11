import ctypes
import glob
import os

def get_recycle_bin_path():
    user = os.getlogin()

    advapi32 = ctypes.windll.advapi32
    lookup = advapi32.LookupAccountNameW

    sid = ctypes.create_unicode_buffer(100)
    sid_size = ctypes.c_uint(100)
    domain = ctypes.create_unicode_buffer(100)
    domain_size = ctypes.c_uint(100)
    sid_type = ctypes.c_uint()

    lookup(None, user, sid, ctypes.byref(sid_size),
           domain, ctypes.byref(domain_size), ctypes.byref(sid_type))

    return fr"C:\$Recycle.Bin\{sid.value}"


def empty_recycle_bin():
    SHERB_NOCONFIRMATION = 0x00000001
    SHERB_NOPROGRESSUI = 0x00000002
    SHERB_NOSOUND = 0x00000004

    ctypes.windll.shell32.SHEmptyRecycleBinW(
        None, None,
        SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND
    )


def delete_by_extension():
    recycle_path = get_recycle_bin_path()
    ext = input("Dame la extensión incluyendo punto -> ")

    files = glob.glob(f"{recycle_path}\\*{ext}")
    count = 0

    for f in files:
        try:
            os.remove(f)
            count += 1
        except Exception as e:
            print(f"Error al eliminar {f}: {e}")

    print(f"Se eliminaron {count} archivos con extensión '{ext}'.")
    input()
    os.system("cls")


def Menu():
    opc = 0
    while opc != 3:
        print("Elige una opción:")
        print("1. Vaciar la papelera completamente")
        print("2. Eliminar archivos por extensión")
        print("3. Salir")

        opc = int(input("opc -> "))

        if opc == 1:
            empty_recycle_bin()
            print("Papelera vaciada con éxito!")
            input()
            os.system("cls")
        elif opc == 2:
            delete_by_extension()


Menu()
