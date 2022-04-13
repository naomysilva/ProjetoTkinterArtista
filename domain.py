import gui
import db


def main():
    gui.tela_menu_principal()


def cadastrar_artista():
    gui.tela_cadastrar_artista()


def dados_artista(Nome_album, Nome_artista, Data_artista, combobox_album):
    global status
    if Nome_album.get() == "" or Nome_artista.get() == "" or Data_artista.get() == "" or combobox_album.get() == "":
        gui.erro()

    else:
        db.salvar_artista(Nome_album, Nome_artista, Data_artista, combobox_album)
        gui.sucesso()


def listagem():
    tudo_do_arquivo = db.listar_tudo()
    gui.tela_listagem(tudo_do_arquivo)


def buscar_artista():
    gui.tela_busca(db.lista_anos())


def pesquisar_nome(nome):
    gui.tela_exibir_busca_por_nome(db.consulta_por_nome(nome))


def pesquisar_data(data, posicao):
    print('posicao = {}'.format(posicao))
    gui.tela_exibir_busca_por_data(db.consulta_por_data(data, posicao))


if __name__ == "__main__":
    main()
