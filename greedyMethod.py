"""
Algoritmia y Complejidad
Entrega: Miercoles 28 Oct. 2020
@steven_wilson
"""

# Ej 1: Programa que determine la secuencia de n trabajos que proporcione el maximo beneficio

trabajos = [1, 2, 3, 4, 5, 6]
plazos = [5, 3, 3, 2, 4, 2]
ganancias = [200, 180, 190, 300, 120, 100]


def cronograma_optimo(trabajos, plazos, ganancias):
    myList = []
    space = list(range(1, max(plazos) + 1))
    optimo = []
    for i in range(len(trabajos)):
        myList.append([trabajos[i], [plazos[i], ganancias[i]]])

    sortedTable = sorted(myList, key=lambda x: x[1][1], reverse=True)
    print("Trabajos ordenados por ganancias (descendiente)", sortedTable)

    for i in range(len(sortedTable)):
        if len(space) != 0:
            if sortedTable[i][1][0] >= space[0]:
                space.pop(0)
                optimo.append(sortedTable[i][0])
            else:
                pass

    print("El orden optimo de los trabajos es: ", optimo)


cronograma_optimo(trabajos, plazos, ganancias)

#  Ej 2: Programa que determine el patron optiom de combiancion de un conjunto de n listas
identificador = ["a", "b", "c", "d", "e", "f"]
datos = [40, 10, 20, 15, 25, 30]


def combinacion_listas(identificador, datos):
    myDict = {}
    count = 0
    operaciones = []
    orden = []
    for i in range(len(datos)):
        myDict[identificador[i]] = datos[i]

    sortedDict = {k: v for k, v in sorted(
        myDict.items(), key=lambda item: item[1])}

    for k, v in sortedDict.items():
        count += v
        operaciones.append(count)
        orden.append(k)

    operaciones.pop(0)
    print("Secuendia de combinacion: ", orden,
          "\n Cantidad de operaciones realizadas", operaciones, " = ", sum(operaciones))


print()
combinacion_listas(identificador, datos)
