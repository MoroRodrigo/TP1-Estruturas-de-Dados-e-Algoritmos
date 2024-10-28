def greatestNumber(array):
    frequencia = {}

    for num in array:
        if num in frequencia:
            frequencia[num] += 1
        else:
            frequencia[num] = 1

    maior_numero_unico = None

    for num, count in frequencia.items():
        if count == 1: 
            if maior_numero_unico is None or num > maior_numero_unico:
                maior_numero_unico = num

    return maior_numero_unico


#Uso
array = [5, 1, 5, 2, 7, 1, 8, 2, 9]
print(greatestNumber(array))
