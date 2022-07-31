import juncao

# 1 - Testa se o valor armazenado em 'a' e 'b' sao os esperados 

def testeArquivo1():
    assert juncao.a == "Arquivo1.txt"

def testeArquivo2():
    assert juncao.b == "Arquivo2.txt"


# 2 - Testa se a funcao "extraiNumeros" consegue obter todo o conteudo do arquivo

def testeExtracaoArquivo1():
    assert juncao.extraiNumeros("Arquivo1.txt") == ['1', '3', '5', '7']

def testeExtracaoArquivo2():
    assert juncao.extraiNumeros("Arquivo2.txt") == ['2', '4', '6']

def testeExtracaoArquivo3():
    assert juncao.extraiNumeros("Arquivo3.txt") == ['1', '2', '3']

def testeExtracaoArquivo4():
    assert juncao.extraiNumeros("Arquivo4.txt") == ['1', '2', '3', '6', '7', '8']


# 3 - Testa se a funcao "juntaNumeros" junta efetivamente as listas numericas de dois arquivos

def testeJuncaoArquivos1e2():
    assert juncao.juntaNumeros("Arquivo1.txt", "Arquivo2.txt") == ['1', '3', '5', '7', '2', '4', '6']

def testeJuncaoArquivos1e3():
    assert juncao.juntaNumeros("Arquivo1.txt", "Arquivo3.txt") == ['1', '3', '5', '7', '1', '2', '3']

def testeJuncaoArquivos1e4():
    assert juncao.juntaNumeros("Arquivo1.txt", "Arquivo4.txt") == ['1', '3', '5', '7', '1', '2', '3', '6', '7', '8']

def testeJuncaoArquivos2e1():
    assert juncao.juntaNumeros("Arquivo2.txt", "Arquivo1.txt") == ['2', '4', '6', '1', '3', '5', '7']

def testeJuncaoArquivos2e3():
    assert juncao.juntaNumeros("Arquivo2.txt", "Arquivo3.txt") == ['2', '4', '6', '1', '2', '3']

def testeJuncaoArquivos2e4():
    assert juncao.juntaNumeros("Arquivo2.txt", "Arquivo4.txt") == ['2', '4', '6', '1', '2', '3', '6', '7', '8']

def testeJuncaoArquivos3e1():
    assert juncao.juntaNumeros("Arquivo3.txt", "Arquivo1.txt") == ['1', '2', '3', '1', '3', '5', '7']

def testeJuncaoArquivos3e2():
    assert juncao.juntaNumeros("Arquivo3.txt", "Arquivo2.txt") == ['1', '2', '3', '2', '4', '6']

def testeJuncaoArquivos3e4():
    assert juncao.juntaNumeros("Arquivo3.txt", "Arquivo4.txt") == ['1', '2', '3', '1', '2', '3', '6', '7', '8']

def testeJuncaoArquivos4e1():
    assert juncao.juntaNumeros("Arquivo4.txt", "Arquivo1.txt") == ['1', '2', '3', '6', '7', '8', '1', '3', '5', '7']

def testeJuncaoArquivos4e2():
    assert juncao.juntaNumeros("Arquivo4.txt", "Arquivo2.txt") == ['1', '2', '3', '6', '7', '8', '2', '4', '6']

def testeJuncaoArquivos4e3():
    assert juncao.juntaNumeros("Arquivo4.txt", "Arquivo3.txt") == ['1', '2', '3', '6', '7', '8', '1', '2', '3']

