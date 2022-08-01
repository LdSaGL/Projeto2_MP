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


def testeJuncaoArquivos1e1():
    assert juncao.juntaNumeros("Arquivo1.txt", "Arquivo1.txt") == ['1', '3', '5', '7', '1', '3', '5', '7']


def testeJuncaoArquivos2e2():
    assert juncao.juntaNumeros("Arquivo2.txt", "Arquivo2.txt") == ['2', '4', '6', '2', '4', '6']


def testeJuncaoArquivos3e3():
    assert juncao.juntaNumeros("Arquivo3.txt", "Arquivo3.txt") == ['1', '2', '3', '1', '2', '3']


def testeJuncaoArquivos4e4():
    assert juncao.juntaNumeros("Arquivo4.txt", "Arquivo4.txt") == ['1', '2', '3', '6', '7', '8', '1', '2', '3', '6', '7', '8']


# 4 - Testa se a funcao "ordenaLista" coloca os termos da lista final em ordem ascendente


def testeJuncaoOrdenada1():
    assert juncao.ordenaLista("Arquivo1.txt", "Arquivo2.txt") == ['1', '2', '3', '4', '5', '6', '7']


def testeJuncaoOrdenada2():
    assert juncao.ordenaLista("Arquivo1.txt", "Arquivo3.txt") == ['1', '1', '2', '3', '3', '5', '7']


def testeJuncaoOrdenada3():
    assert juncao.ordenaLista("Arquivo1.txt", "Arquivo4.txt") == ['1', '1', '2', '3', '3', '5', '6', '7', '7', '8']


def testeJuncaoOrdenada4():
    assert juncao.ordenaLista("Arquivo2.txt", "Arquivo3.txt") == ['1', '2', '2', '3', '4', '6']


def testeJuncaoOrdenada5():
    assert juncao.ordenaLista("Arquivo2.txt", "Arquivo4.txt") == ['1', '2', '2', '3', '4', '6', '6', '7', '8']


def testeJuncaoOrdenada6():
    assert juncao.ordenaLista("Arquivo3.txt", "Arquivo4.txt") == ['1', '1', '2', '2', '3', '3', '6', '7', '8']


def testeJuncaoOrdenada7():
    assert juncao.ordenaLista("Arquivo1.txt", "Arquivo1.txt") == ['1', '1', '3', '3', '5', '5', '7', '7']


def testeJuncaoOrdenada8():
    assert juncao.ordenaLista("Arquivo2.txt", "Arquivo2.txt") == ['2', '2', '4', '4', '6', '6']


def testeJuncaoOrdenada9():
    assert juncao.ordenaLista("Arquivo3.txt", "Arquivo3.txt") == ['1', '1', '2', '2', '3', '3']


def testeJuncaoOrdenada10():
    assert juncao.ordenaLista("Arquivo4.txt", "Arquivo4.txt") == ['1', '1', '2', '2', '3', '3', '6', '6', '7', '7', '8', '8']


# 5 - Testa se o arquivo final foi criado e esta formatado com os valores esperados


def testeArquivoFinal1():
    assert open('Juncao12.txt', 'r').read().splitlines() == ['1', '2', '3', '4', '5', '6', '7']


def testeArquivoFinal2():
    assert open('Juncao13.txt', 'r').read().splitlines() == ['1', '1', '2', '3', '3', '5', '7']


def testeArquivoFinal3():
    assert open('Juncao14.txt', 'r').read().splitlines() == ['1', '1', '2', '3', '3', '5', '6', '7', '7', '8']


def testeArquivoFinal4():
    assert open('Juncao23.txt', 'r').read().splitlines() == ['1', '2', '2', '3', '4', '6']


def testeArquivoFinal5():
    assert open('Juncao24.txt', 'r').read().splitlines() == ['1', '2', '2', '3', '4', '6', '6', '7', '8']


def testeArquivoFinal6():
    assert open('Juncao34.txt', 'r').read().splitlines() == ['1', '1', '2', '2', '3', '3', '6', '7', '8']


def testeArquivoFinal7():
    assert open('Juncao11.txt', 'r').read().splitlines() == ['1', '1', '3', '3', '5', '5', '7', '7']


def testeArquivoFinal8():
    assert open('Juncao22.txt', 'r').read().splitlines() == ['2', '2', '4', '4', '6', '6']


def testeArquivoFinal9():
    assert open('Juncao33.txt', 'r').read().splitlines() == ['1', '1', '2', '2', '3', '3']


def testeArquivoFinal10():
    assert open('Juncao44.txt', 'r').read().splitlines() == ['1', '1', '2', '2', '3', '3', '6', '6', '7', '7', '8', '8']
