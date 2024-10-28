import random

baralho_espadas = list(range(1, 14))

random.shuffle(baralho_espadas)


def ordenar_cartas_embaralhadas(cartas):
    mao_ordenada = []
    
    for carta in cartas:
        if not mao_ordenada:
            mao_ordenada.append(carta)
        else:
            inserida = False
            for i in range(len(mao_ordenada)):
                if carta < mao_ordenada[i]:
                    mao_ordenada.insert(i, carta)
                    inserida = True
                    break
            
            if not inserida:
                mao_ordenada.append(carta)
    
    return mao_ordenada

cartas_ordenadas = ordenar_cartas_embaralhadas(baralho_espadas)

print("Cartas embaralhadas:", baralho_espadas)
print("Cartas ordenadas:", cartas_ordenadas)
