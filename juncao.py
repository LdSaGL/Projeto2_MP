""" Funcao que extrai os numeros de um arquvio e retorna uma lista"""
def extraiNumeros(x):
    arquivoAberto = open(x, 'r')
    numerosArquivo = []
    for numero in arquivoAberto:
        numerosArquivo.append(numero.strip())
    arquivoAberto.close()
    return numerosArquivo

""" Funcao que junta as listas extraidas de cada um dos dois arquivos e retorna uma lista"""
def juntaNumeros(a, b):
    print()

""" Funcao que pega a lista obtida na funcao juntaNumeros, ordena e retorna uma lista"""
def ordenaNumeros(a, b):

    return

""" Funcao que cria o arquivo final e coloca os numeros da lista ordenada seguindo o padrao de formatacao fornecido no roteiro"""
def executar(a, b):
    ordenaNumeros
    print()

print('Me informe quais os arquivos que deverao ser unidos seguindo o formato : "NomeDoArquivo.txt"')
#a = input('Primeiro arquivo: ')
#b = input('Segundo arquivo: ')
a = "Arquivo1.txt"
b = "Arquivo2.txt"
c = "Arquivo3.txt"
d = "Arquivo4.txt"

print(extraiNumeros(a))


