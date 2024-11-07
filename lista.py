###funcion imprime que reciba una lista###
"""
def imprime(lista):
    for x in lista:
        print(f'{x}' , end = '')
    print

imprime([2,3,7,5,1,])
 
def imprimeR(lista):
    if lista == []:
        return
    imprimeR(lista[1:])
    print(f'{lista[0]},',end='')
    return

imprimeR([2,3,7,5,1,])

"""

###función recursiva que diga si existe o no un número

def buscarNumero(lista, num):
    if lista == []:
        return False
    if lista[0] == num:
        return True
    return buscarNumero(lista[1:], num)

lista = [2,5,4,1,9]
num = 5

if buscarNumero(lista, num):
    print(f"El numero {num} existe en la lista.")
else:
    print(f"El numero {num} NO existe en la lista.")
    
# para entregar:
# 1: formulación recursiva del ordenamiento por intercambio
# 2: formulación recursiva de la busqueda de un elemento y regresa -1 si no existe
# y el indice del número si existe (no usar ninguna función de las listas de python)