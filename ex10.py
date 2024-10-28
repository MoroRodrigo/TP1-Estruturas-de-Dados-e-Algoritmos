def bubbleSortStrings(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Teste 1: Lista de strings desordenadas
lista1 = ["banana", "maçã", "laranja", "uva", "abacaxi"]
print("Lista 1 ordenada:", bubbleSortStrings(lista1))

# Teste 2: Lista já ordenada
lista2 = ["a", "b", "c", "d"]
print("Lista 2 ordenada:", bubbleSortStrings(lista2))

# Teste 3: Lista em ordem reversa
lista3 = ["z", "y", "x", "w", "v"]
print("Lista 3 ordenada:", bubbleSortStrings(lista3))

# Teste 4: Lista com strings duplicadas
lista4 = ["banana", "maçã", "banana", "laranja"]
print("Lista 4 ordenada:", bubbleSortStrings(lista4))

# Teste 5: Lista vazia
lista5 = []
print("Lista 5 ordenada:", bubbleSortStrings(lista5))

# Teste 6: Lista com um único elemento
lista6 = ["a"]
print("Lista 6 ordenada:", bubbleSortStrings(lista6))
