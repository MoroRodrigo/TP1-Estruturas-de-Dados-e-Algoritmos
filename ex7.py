def selectAStrings(array):
    newArray = []

    for i in range(len(array)):
        if array[i].startswith("a"):
            newArray.append(array[i])

    return newArray


print("A complexidade total da função é dominada pelo loop, resultando em:")
print("O(n)")
print("onde 'n' é o número de strings no array de entrada.")