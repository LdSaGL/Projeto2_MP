""" Funcao que extrai os numeros de um arquvio e retorna uma lista"""
def extraiNumeros(z):
    arquivoAberto = open(z, 'r')
    numerosArquivo = []
    for numero in arquivoAberto:
        numerosArquivo.append(numero.strip())
    arquivoAberto.close()
    return numerosArquivo

""" Funcao que junta as listas extraidas de cada um dos dois arquivos e retorna uma lista"""
def juntaNumeros(arquivoX, arquivoY):
    lista_X = extraiNumeros(arquivoX)
    lista_Y = extraiNumeros(arquivoY)
    lista_X.extend(lista_Y)
    return lista_X

""" Funcao que pega a lista obtida na funcao juntaNumeros, ordena e retorna uma lista"""
def ordenaLista(arquivoX, arquivoY):
    lista_unida = juntaNumeros(arquivoX, arquivoY)
    lista_unida.sort()
    return lista_unida

""" Funcao que cria o arquivo final e coloca os numeros da lista ordenada seguindo o padrao de formatacao fornecido no roteiro"""
def executar(arquivoX, arquivoY, nomeArquivo):
    lista = ordenaLista(arquivoX, arquivoY)
    arquivo_final = open(nomeArquivo, "x")
    for termo in lista:
        arquivo_final.write(termo+'\n')


a = "Arquivo1.txt"
b = "Arquivo2.txt"


"""print('Informe quais os arquivos que deverao ser unidos seguindo o formato: "NomeDoArquivo.txt"')
a = input('Primeiro arquivo: ')
b = input('Segundo arquivo: ')
print()
print('Informe como deseja chamar o arquivo final seguindo o formato: "NomeDoArquivo.txt"')
nome = input('Nome do arquivo: ')
executar(a, b, nome)"""
