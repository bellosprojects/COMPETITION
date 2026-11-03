# Javier Garcia
# Recuerda no usar librerias externas
# Usa get_data() para leer los datos separados por espacios
# Usa print() para devolver los resultados
# No imprimas lineas o espacios demas

import base64, marshal
exec(marshal.loads(base64.b64decode(b'4wAAAAAAAAAAAAAAAAIAAAAAAAAA8xYAAACAAC4AdABSABcAUgEXAGwQdAFSAiMAKQNjAQAAAAEAAAAAAAAAAgAAAAMAAADzJAAAAIAAVgBeAjiEAABkAwAAHABRAWgBUgFcAAAAAAAAAAAALwEjACkC6QIAAADaBnJldHVybikB2gNzdHIpAdoGZm9ybWF0cwEAAAAi2gg8c3RyaW5nPtoMX19hbm5vdGF0ZV9fcggAAAACAAAAcxMAAACAAPcABgEj8QAGASOUA/EABgEj8wAAAABjAAAAAAAAAAAAAAAABAAAAAMAAADzEAEAAIAAXAEAAAAAAAAAAFwCAAAAAAAAAAA0AQAAAAAAAF4AOFgAAGRJAAAcABsAXAUAAAAAAAAAADQAAAAAAAAAUAcAAAAAAAAAAAAAAAAAAAAAAAA0AAAAAAAAAHAAVgAnAAAAAAAAAGQmAAAcAFwCAAAAAAAAAABQCQAAAAAAAAAAAAAAAAAAAAAAAFYAUAsAAAAAAAAAAAAAAAAAAAAAAAA0AAAAAAAAADQBAAAAAAAAHwBLWgAAS1wAAFwCAAAAAAAAAAAnAAAAAAAAAGQWAAAcAFwCAAAAAAAAAABQDQAAAAAAAAAAAAAAAAAAAAAAAF4ANAEAAAAAAAAjAFIBIwAgAB8AHQBLKAAAOwMdAGkBKQLpAAAAANoAKQfaA2xlbtoCX3PaBWlucHV02gVzdHJpcNoGZXh0ZW5k2gVzcGxpdNoDcG9wKQHaAl90cwEAAAAgcgcAAADaCGdldF9kYXRhchUAAAACAAAAc1UAAACAANwKDYxiiyeQQYwc8AIDCRbcERaTF5cdkR2TH4hC3w8RlDKXOZE5mFKfWJlYm1rWEyiJcucYGpsCjDKPNok2kCGLOdAEIqAC0AQi+PADAAkWkgX6cwwAAACWQQNCAADCAAJCBQNOKQJyDgAAAHIVAAAAqQByCQAAAHIHAAAA2gg8bW9kdWxlPnIXAAAAAQAAAHMPAAAA8AMBAQHYAwWAAvcCBgEjcgkAAAA=')))


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