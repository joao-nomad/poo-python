## Desenvolvedor: JOÃO VITOR LESSA BARROS ##
## POO - Programação Orientada a Objetos ##
## Professor Orientador: Renzo Nuccitelli ##

## Técnica que o professor indicou em sala de aula para iniciar##
## Criamos uma variável só, com todos os numeros e separamos pelo traço ##
valores = 'Zero-Um-Dois-Três-Quatro-Cinco-Seis-Sete-Oito-Nove'.split("-")


## Função para transformar número inteiro em texto ##
def converterNumero(numero):
    resultado = ""
    for cont in str(numero):
        resultado = resultado + valores[int(cont)] + " - "        
    return resultado[:-2]
    ## Tive que fatiar a lista para evitar de exibir o traço no último número ##


## Encontrei um pouco de dificuldade para converter de volta para String, achei que só a função INDEX de lista fosse resolver meu problema##
def encontrarIndex(string):
    index = str(valores.index(string))
    return index

## Porém, se eu digitasse mais de um número ia dar problema, então procurando por alternativas, achei a função MAP ##
def converterString(string):
    algarismo = string.split(" - ")
    resultado = ""
    indice = list(map(encontrarIndex, algarismo))

    for cont in indice:
        resultado = resultado + cont

    return int(resultado)

## Testando função para converter Inteiros ##
assert "Um - Dois - Três " == converterNumero(123)
assert "Três - Dois - Um " == converterNumero(321)
    
## Testando função para converter Strings ##
assert 789 == converterString("Sete - Oito - Nove")
assert 987 == converterString("Nove - Oito - Sete")
