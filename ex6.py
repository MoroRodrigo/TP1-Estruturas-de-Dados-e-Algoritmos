def encontrar_quadrado(grains):
    if grains < 1:
        return "Quantidade de grãos deve ser 1 ou mais."

    quadrado = 1
    quantidade = 1  

    while quantidade < grains:
        quadrado += 1
        quantidade *= 2 

    return quadrado

# Testando
resultado = encontrar_quadrado(16)
print(resultado) 


print("A complexidade de tempo da função pode ser descrita como 𝑂(log n), onde n é a quantidade de grãos de arroz fornecida.")
