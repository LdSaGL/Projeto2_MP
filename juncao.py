def extraiNumeros(arquivo):
    """
    Funcao que extrai os numeros de um arquvio e retorna uma lista

    :param arquivo: str

    :return list numerosArquivo:
    """
    arquivoAberto = open(arquivo, 'r')
    numerosArquivo = []
    for numero in arquivoAberto:
        numerosArquivo.append(numero.strip())
    arquivoAberto.close()
    return numerosArquivo


def juntaNumeros(arquivoX, arquivoY):
    """
    Funcao que junta as listas extraidas de cada um dos dois arquivos e
    retorna uma lista

    :param arquivoX: str
    :param arquivoX: str

    :return list listaNumerica:
    """
    lista_numerica = extraiNumeros(arquivoX)
    lista_numerica_auxiliar = extraiNumeros(arquivoY)
    lista_numerica.extend(lista_numerica_auxiliar)
    return lista_numerica


def ordenaLista(arquivoX, arquivoY):
    """
    Funcao que pega a lista obtida na funcao juntaNumeros, ordena e
    retorna uma lista

    :param arquivoX: str
    :param arquivoX: str

    :return list lista_unida:
    """
    lista_unida = juntaNumeros(arquivoX, arquivoY)
    lista_unida.sort()
    return lista_unida


def executar(arquivoX, arquivoY, nomeArquivo):
    """
    Funcao que cria o arquivo final e coloca os numeros da lista
    ordenada seguindo o padrao de formatacao fornecido no roteiro

    :param arquivoX: str
    :param arquivoX: str
    :param nomeArquivo: str
    """
    lista = ordenaLista(arquivoX, arquivoY)
    arquivo_final = open(nomeArquivo, "x")
    for termo in lista:
        arquivo_final.write(termo+'\n')


# Variaveis de teste - desconsiderar ao rodar o codigo
a = "Arquivo1.txt"  # comentar a linha para rodar
b = "Arquivo2.txt"  # comentar a linha para rodar

""" <- Excluir para rodar
print('Siga o formato para qualquer input: "NomeDoArquivo.txt"')
print('Informe quais os arquivos que deverao ser unidos')
a = input('Primeiro arquivo: ')
b = input('Segundo arquivo : ')
print()
print('Informe como deseja nomear o arquivo final')
nome = input('Nome do arquivo: ')
executar(a, b, nome)
Excluir para rodar -> """
