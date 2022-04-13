from tkinter import END
import ast

def listar_tudo():
    tudo =[]
    with open("nomes.txt", "r", encoding="utf-8") as file:
        for x in file.readlines():
            tudo.append(x)
    return tudo

def salvar_artista(Nome_album,Nome_artista,Data_artista,combobox_album):

    with open("nomes.txt", "a", encoding="utf-8") as file:
        file.write(
            f"nome do album: {Nome_album.get()}| nome do artista: {Nome_artista.get()}| data de lancamento do album: {Data_artista.get()}| ultimo album lançado: {combobox_album.get()}|\n")
        Nome_album.delete(0, END)
        Nome_artista.delete(0, END)
        Data_artista.delete(0, END)
        combobox_album.set("")

def lista_anos():
    global lista_combobox_ano
    with open("nomes.txt", "r", encoding="utf-8") as file:
        lista_combobox_ano = []
        for x in file.readlines():
            lista_ano = []
            separador = x.split("|")
            lista_ano.append(separador[2])
            lista_ano = "".join(lista_ano)
            if lista_ano[30:] in lista_combobox_ano:
                pass
            else:
                lista_combobox_ano.append(lista_ano[30:])
    return lista_combobox_ano


def consulta_por_nome(nome):
    nomes = []
    with open("nomes.txt", "r", encoding="utf-8") as file:
        for x in file.readlines():
            separador = x.split("|")
            nome_do_artista = separador[1]
            nome_do_artista = nome_do_artista.split(':')
            nome_do_artista = nome_do_artista[1].strip()
            if nome in nome_do_artista:
                nomes.append(x)
    return nomes


def consulta_por_data(data, parametro):
    nomes = []
    with open("nomes.txt", "r", encoding="utf-8") as file:
        for x in file.readlines():
            separador = x.split("|")
            ano_lancamento = separador[2]
            ano_lancamento = ano_lancamento.split(':')
            ano_lancamento = ano_lancamento[1].replace(' ', '')
            print(data, ano_lancamento)
            if data != '':
                if parametro == 1 and data >= ano_lancamento:
                    nomes.append(x)
                elif parametro == 2 and data == ano_lancamento:
                    nomes.append(x)
                elif parametro == 3 and data <= ano_lancamento:
                    nomes.append(x)
    print(parametro, 'nomes:\n',nomes)
    return nomes