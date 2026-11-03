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

    pass # Tu codigo aqui

if __name__ == "__main__":
    main()