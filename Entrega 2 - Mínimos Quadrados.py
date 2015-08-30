## Desenvolvedor: JOÃO VITOR LESSA BARROS ##
## POO - Programação Orientada a Objetos ##
## Professor orientador: Renzo Nuccitelli ##

## Capturando input do usuário ##
print("## Entrega 2 - Mínimos Quadrados ##")
inteiro = int(input("\nInsira um inteiro não-negativo: "))


## Gerando os quadrados de X ##
def gerar_quadrado(x):
    fileira = []
    for cont in range (1, x+1):
        valor = cont ** 2
        if valor <= x:
            fileira.append(valor)
    return fileira


## Diminuindo a lista ##
def compactar(x, fileira):
    fileira2 = []
    tamanho = len(fileira)-1
    while sum(fileira2) != x:
        if (fileira[tamanho] + sum(fileira2)) <= x:
            fileira2.append(fileira[tamanho])
        else:
            tamanho = tamanho - 1
    return fileira2


## Função Final para exibir o resultado e tratar os valores da lista ##
def calcular(x):
    if x == 0:
        return 0
    elif x in gerar_quadrado(x):
        return x
    else:
        fileira = gerar_quadrado(x)
        fileira2 = compactar(x, fileira)
        while fileira:
            if len(compactar(x, fileira)) < len(fileira2):
                fileira2 = compactar(x, fileira)
            else:
                fileira.pop()
        return fileira2

## Chamando a função principal com um Input inserido pelo usuário ##
resultado = calcular(inteiro)
## Imprimindo resultado final ##
print("Mínimo(s) quadrados: ")
print(inteiro, resultado)
