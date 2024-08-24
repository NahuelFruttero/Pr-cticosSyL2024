"""
Evaluación diagnóstica de la resolución algorítmica de un problema.
Partiendo de las operaciones sobre conjuntos, realizar un algoritmo en
donde dado 2 conjuntos se determinen / verifiquen las operaciones de:

2- INTERSECCIÓN DE CONJUNTOS
Dados dos conjuntos A={1,2,3,4,5} y B={4,5,6,7,8,9} la intersección de estos
conjuntos será A∩B={4,5}
"""

conjuntoA = [1,2,3,4,5]
conjuntoB = [4,5,6,7,8,9]

conjuntoAUB = []

for elemento in conjuntoA:
    if elemento in conjuntoB:
        estaEnConjunto = True
    else:
        estaEnConjunto = False

    if estaEnConjunto == True:
        conjuntoAUB.append(elemento)

print('El conjunto A es:')
print(conjuntoA)
print('El conjunto B es:')
print(conjuntoB)
print('El conjunto AUB es:')
print(conjuntoAUB)