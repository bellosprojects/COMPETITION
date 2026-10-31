# Enunciados Competencia

Aqui se muestran todos los enunciados de los problemas a resolver en esta competencia.

Recuerda antes haber:

* Instalado Python
* Forkeado este repo
* Crear tu rama
* Llenar la planilla del PR

Puedes probar tu solucion antes de enviarla:

```bash
python "soluciones/solucionX.py"
```

Donde `X` es el numero de la solucion que quieres probar.

---
*No puedes usar librerias externas*

*No modifiques el nombre de los archivos de solucion*


Cuando tengas lista tu solucion:

* Prepara todos tus cambios `Stage All Changes`
* Has `Commit & Push`
* Veras tus resultados en el canal `#results` de discord.


> **Importante:** Toda la entrada/salida es por stdin/stdout. Se debe imprimir una unica linea por archivo.



## Problema 1
Un usuario de avion quiere verificar si el ticket que le proporciono la aerolinea es legitimo. Para esto visita la web oficial de la aerolinea donde le indican los pasos para esta verificacion:

* Los digitos del 1 al 5 digitos corresponden a la marca del avion
* Los digitos del 6 al 10 corresponden al modelo del avion
* Los digitos del 11 al 15 corresponden al numero del validez
* El resto de los digitos digitos corresponden a su numero de asiento
* La cantidad de asientos disponibles no alcanza a la marca pero si al modelo
* El numero de validez no aporta digitos nuevos al ticket
* El modelo mas la validez supera la cantidad maxima de asientos permitidos en el avion

Desarrolle un algoritmo en python que reciba el ticket del usuario e imprima `0` o `1` indicando si el ticket es falso o legitimo respectivamente.

Ejemplos:
```
in:
00343005904032134

out:
0
```
---
```
in:
720430034572553498

out:
1
```

## Problema 2
En la fabricacion de chips se requiere comprobar el funcionamiento actual de los cirtucitos fabricados. El estandar de la fabrica usa los codigos:

* `N`: Para la compuerta not
* `O`: Para la compuerta or
* `A`: Para la compuerta and

Ademas se establecen canales de comunicacion con identificacion numerica. Cada compuerta recive primero su(s) canal(es) de entrada y al final su canal de salida. Ej:

```Python
1 2 A 3

#Indica que la compuerta AND recibe la señal de los canales 1 y 2, y, manda el resultado al canal 3
```

Todas las compuertas se ejecutan simultaneamente en cada tick.

Diseñe un algoritmo en python que dado el tick objetivo, el canal de salida, el numero de compuertas y la lista de compuertas, imprima el valor de ese canal en ese tick de la forma:

* `1`: Activo
* `0`: Inactivo

***Todos los canales inician (tick 0) en 0***


Ejemplos:
```
in:
2 4 3
1 N 2
2 3 O 4
4 N 4

out:
1
```
```
in:
4 7 5
0 1 O 2
3 5 O 4
2 4 A 7
1 N 3
7 N 0

out:
1
```

## Problema 3
Las pantallas tactiles requieren interpretar que boton o parte de la pantalla selecciono el usuario cuando toca la panatalla. Para eso las aplicaciones registran sus botones de la forma:

```
ID_BOTON NUM_PIXELES PIXEL1, PIXEL2, ..., PIXELN
```

Donde PIXELX es un numero entero que representa su ubicacion de la pantalla

Para saber que toco el usuario, el sistema calcula cual es el punto mas cercano (X y X + 1 son lo mas cercano que hay). En caso de que el pixel no pertenezca a ningun boton su activa una tolerancia de distancia correspondiente al NUM_PIXELES de cada boton. Si aun asi ninguno supera el umbral se asume que el toque fue al fondo de la app.

Diseñe un algoritmo el python que dado el pixel tocado por el usuario, el numero de botones y la lista de botones imprima:

* `ID_BOTOM`: Si se cree que el usuario toco un boton
* `-1`: Si se cree que el usuario toco el fondo de la app.

Ejemplos:
```
in:
45 4
102 4 40 41 42 43
103 4 50 51 52 53
104 4 47 46 45 44
105 4 30 31 32 33

out:
104
```
```
in:
8932 6
456 6 8912 8962 8922 8942 8272 8942
457 4 455 8944 522 434
458 3 3493 3423 3424
459 8 748 837 372 243 433 468 423 348
460 2 9843 2342
461 5 98435 345345 435355 24231 23132

out:
-1
```

## Problema 4
Para llevar el control de construccion de una casa, un arquitecto calcula los pasos necesarios para ir desde cualquier punto de la casa a otro. Cada habitacion tiene un largo y un ancho y cada pasillo un largo. 

Asumiendo que el ancho y largo de las habitaciones y pasillos se miden en pasos:

Diseñe un algoritmo en python que dada una lista de habtaciones y pasillos diga si es posible llegar de cualquier punto a cualquier otro punto de la casa en menos de `2 * cantidad de habitaciones - cantidad de pasillos + 1` pasos.

La salida es:

* `1`: Si es posibles
* `0`: Si no es posible

*Nota: Considere la distancia mas larga dentro de una habitacion como la distancia a recorrer. Ademas: la distancia para ir de A a B es tamaño de A + largo del pasillo A-B + tamaño de B*

El formato de entrada es:

```
NUM_HABITACIONES NUM_PASILLOS
ID_HAB1 LARGO_HAB1 ANCHO_HAB1
ID_HAB2 LARGO_HAB2 ANCHO_HAB2
...
ID_HAB3 LARGO_HABN ANCHO_HABN
ID_PASILLO1 LARGO_PASILLO1 ID_HAB_ORIGEN ID_HAB_DESTINO
ID_PASILLOM LARGO_PASILLOM ID_HAB_ORIGEN ID_HAB_DESTINO
```

Un pasillo que va de 1 a 2 implica que tambien se puede ir de 2 a 1 por el mismo pasillo.

*Asuma que todas las habitaicones estan conectadas por al menos un pasillo con otras*

Ejemplos:
```
in:
4 3
0 1 2
1 1 4
2 3 5
3 1 2
4 2 0 1
5 2 0 2
6 1 0 3

out:
0
```
```
in:
2 1
0 1 1
1 1 1
2 1 0 1

out:
1
```

## Problema 5
Cuando se trata de programar un sistema de alto riesgo como el de un avion o uno medico, la presicion no se discute, debe ser la maxima. Usando expresiones comunes esta presicion se pierde, ej. el siguiente codigo python
```python
A = 0.2
B = 0.1

print(A + B == 0.3) # Imprime False
```

Tu mision es implementar un sistema numerico que sea capaz de almacenar n decimales con absoluta presicion para realizar calculos picometricos.

Ademas de esto, como tu sistema no es nativo en python tendras que realizar un pequeño parser que soporte las operaciones `+`, `-` y `=`.

El formato de entrada es:
```
NUM_VARS
NOMBRE_VAR1 VALOR_VAR1
NOMBRE_VAR2 VALOR_VAR2
...
NOMBRE_VARN VALOR_VARN
EXPRESION
```

Solo se debe imprimir el resultado de la expresion (bool si es una comparacion o numero de alta presicion si es una operacion aritmetica)

***Las operaciones aritmeticas se resuelven primero***

***No se puede perder ni un solo decimal***

Ejemplos:
```
in:
3
A 0.1
B 0.2
C 0.3
A + B = C

out:
True
```

```
in:
4
A 0.00005
B 0.00000000005
C 1.000000000000000255
D 0.00000000022144
A + B - C + D

out:
-0.999949999728560255
```