def get_data(_=[iter(())]):
 while 1:
  try:return next(_[0])
  except StopIteration:_[0]=iter(input().strip().split())

def main():

    ticket = get_data()

    marca = ticket[0:5]
    modelo = ticket[5:10]
    validez = ticket[10:15]
    asiento = ticket[15:]

    marca_i = int(marca)
    modelo_i = int(modelo)
    validez_i = int(validez)
    asiento_i = int(asiento)

    if not (modelo_i <= asiento_i < marca_i):
      print(0)
    elif not (set(validez).issubset(set(marca + modelo + asiento))):
      print(0)
    elif not (modelo_i + validez_i > marca_i):
      print(0)
    else:
      print(1)

if __name__ == "__main__":
 main()