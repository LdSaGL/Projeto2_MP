import juncao

def testeArquivosAbertos():
    assert juncao.arquivos("Arquivo1", "Arquivo2") == ("Arquivo1.txt", "Arquivo2.txt")