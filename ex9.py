def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
    
    return arr

# Teste 1: Lista de números desordenados
lista1 = [64, 34, 25, 12, 22, 11, 90]
print("Lista 1 ordenada:", bubbleSort(lista1))

# Teste 2: Lista já ordenada
lista2 = [1, 2, 3, 4, 5]
print("Lista 2 ordenada:", bubbleSort(lista2))

# Teste 3: Lista em ordem decrescente
lista3 = [5, 4, 3, 2, 1]
print("Lista 3 ordenada:", bubbleSort(lista3))

# Teste 4: Lista com elementos duplicados
lista4 = [3, 1, 2, 3, 5, 3]
print("Lista 4 ordenada:", bubbleSort(lista4))

# Teste 5: Lista vazia
lista5 = []
print("Lista 5 ordenada:", bubbleSort(lista5))

# Teste 6: Lista com um único elemento
lista6 = [42]
print("Lista 6 ordenada:", bubbleSort(lista6)) 
