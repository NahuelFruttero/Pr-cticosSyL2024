"""
Evaluación diagnóstica de la resolución algorítmica de un problema.
Partiendo de las operaciones sobre conjuntos, realizar un algoritmo en
donde dado 2 conjuntos se determinen / verifiquen las operaciones de:

1- UNIÓN DE CONJUNTOS
Dados dos conjuntos A={1,2,3,4,5,6,7,} y B={8,9,10,11} la unión de estos conjuntos
será A∪B={1,2,3,4,5,6,7,8,9,10,11}
"""

conjuntoA = [1,2,3,4,5,6,7]
conjuntoB = [8,9,10,11]

conjuntoAUB = []

for elemento in conjuntoA:
    if elemento in conjuntoAUB:
        estaEnConjunto = True
    else:
        estaEnConjunto = False

    if estaEnConjunto == False:
        conjuntoAUB.append(elemento)

for elemento in conjuntoB:
    if elemento in conjuntoAUB:
        estaEnConjunto = True
    else:
        estaEnConjunto = False

    if estaEnConjunto == False:
        conjuntoAUB.append(elemento)


print('El conjunto A es:')
print(conjuntoA)
print('El conjunto B es:')
print(conjuntoB)
print('El conjunto AUB es:')
print(conjuntoAUB)