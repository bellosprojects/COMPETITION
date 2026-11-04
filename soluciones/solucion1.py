# Javier Garcia
# Recuerda no usar librerias externas
# Usa get_data() para leer los datos separados por espacios
# Usa print() para devolver los resultados
# No imprimas lineas o espacios demas
# Funcion de lectura, NO MODIFICAR
def get_data(_=[iter(())]):
    while 1:
        try:return next(_[0])
        except StopIteration:_[0]=iter(input().strip().split())

def main() -> None:
    ticket = get_data()
    marca = ticket[0:5]
    modelo = ticket[5:10]
    validez = ticket[10:15]
    asiento = ticket[15:]

    mar_i = int(marca)
    mod_i = int(modelo)
    val_i = int(validez)
    asi_i = int(asiento)

    if not( mod_i <= asi_i < mar_i):
        print(0)
    elif not set(validez).issubset(marca+modelo+asiento):
        print(0)
    elif val_i + mod_i <= mar_i:
        print(0)
    else:
        print(1)

if __name__ == "__main__":
    main()