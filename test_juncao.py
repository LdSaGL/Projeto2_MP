import juncao

# 1 - Testa se o valor armazenado em 'a' e 'b' sao os esperados 

def testeArquivo1():
    assert juncao.a == "Arquivo1.txt"

def testeArquivo2():
    assert juncao.b == "Arquivo2.txt"


# 2 - Testa se a funcao extraiNumeros consegue obter todo o conteudo do arquivo

def testeExtracaoArquivo1():
    assert juncao.extraiNumeros("Arquivo1.txt") == ['1', '3', '5', '7']

def testeExtracaoArquivo2():
    assert juncao.extraiNumeros("Arquivo2.txt") == ['2', '4', '6']

def testeExtracaoArquivo3():
    assert juncao.extraiNumeros("Arquivo3.txt") == ['1', '2', '3']

def testeExtracaoArquivo4():
    assert juncao.extraiNumeros("Arquivo4.txt") == ['1', '2', '3', '6', '7', '8']

