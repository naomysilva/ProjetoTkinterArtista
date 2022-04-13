from tkinter import *
from tkinter import ttk

import tk as tk

import domain
import os

janela = Tk()

def tela_listagem(tudo):
    global janela
    janela.destroy()
    janela = Tk()
    janela.title("                                                                          Lista resultado")
    janela.config(background="lightblue")
    janela.geometry("700x550")
    janela.maxsize(width=900, height=700)
    variavel_mudanca = 0
    for x in tudo:
        Label(janela, text=x, background="white").place(x=5, y=variavel_mudanca)
        variavel_mudanca += 20
    botao("Voltar", x=345, y=500, acao=tela_menu_principal)


def tela_busca(anos):
    global janela, Nome
    var = StringVar()
    var.set('0')
    print('parametro', var)
    janela.destroy()
    janela = Tk()
    janela.title("                                                                          Buscar Artistas")
    janela.config(background="lightblue")
    janela.geometry("700x550")
    janela.maxsize(width=900, height=700)
    Label(janela, text="Pesquisa por nome banda/artista:", activebackground="blue", width=25).place(x=50, y=50)
    Nome = Entry(janela, width=30)
    Nome.place(x=50, y=80)
    botao_pesquisar_nome = Button(janela, text="Pesquisar", command=lambda: domain.pesquisar_nome(Nome.get()))
    Label(janela, text="Pesquisa por ano:", activebackground="blue", width=25).place(x=270, y=50)

    radio_variable = StringVar()
    radio_variable.set('Igual')

    anterior = Radiobutton(janela, text='Anterior', variable=radio_variable, value='Anterior')
    anterior.place(x=270, y=80)
    igual = Radiobutton(janela, text='Igual', variable=radio_variable, value='Igual')
    igual.place(x=270, y=110)
    posterior = Radiobutton(janela, text='Posterior', variable=radio_variable, value='Posterior')
    posterior.place(x=270, y=140)
    botao_pesquisar_nome.place(x=50, y=120)
    combobox_ano = ttk.Combobox(janela, values=anos, width=25)
    combobox_ano.place(x=270, y=180)
    x = var.get()
    print('parametro', var)
    print('x', x)
    botao_pesquisar_data = Button(
        janela, text="Pesquisar data", command=lambda: domain.pesquisar_data(combobox_ano.get(), 1 if radio_variable.get() == 'Anterior' else 2 if radio_variable.get() == 'Igual' else 3)
    )
    botao_pesquisar_data.place(x=270, y=220)
    botao("Voltar", x=345, y=500, acao=tela_menu_principal)
    janela.mainloop()


def tela_exibir_busca_por_nome(nomes):
    global janela
    janela.destroy()
    janela = Tk()
    janela.title(        "                                                                          Lista resultado")
    janela.config(background="lightblue")
    janela.geometry("900x900")
    janela.maxsize(width=900, height=900)
    variavel_mudanca = 0
    for x in nomes:
        Label(janela, text=x, background="white").place(x=0, y=variavel_mudanca)
        variavel_mudanca += 20

    janela.mainloop()

def tela_exibir_busca_por_data(datas):
    global janela
    janela.destroy()
    janela = Tk()
    janela.title(        "                                                                          Lista resultado")
    janela.config(background="lightblue")
    janela.geometry("900x900")
    janela.maxsize(width=900, height=900)
    variavel_mudanca =0
    for x in datas:
        Label(janela, text=x, background="white").place(x=0, y=variavel_mudanca)
        variavel_mudanca += 20

    janela.mainloop()


def botao(texto,x,y,acao):
    botao = Button(janela, text=texto, activebackground="blue", bg="lightblue", width=50, command=acao)
    botao.place(x=x, y=y)


def botoes_menu():
    global janela
    botao('Cadastrar Artista',170,330,domain.cadastrar_artista)
    botao('Listagem',170,370,domain.listagem)
    botao('Buscar',170,410,domain.buscar_artista)
    botao('Sair',170,450,janela.destroy)

def tela_menu_principal() :
    global janela
    janela.destroy()
    janela = Tk()
    janela.title("                                                                          Menu Principal")
    janela.config(background="lightblue")
    janela.geometry("700x550")
    janela.maxsize(width=900, height=700)
    img = PhotoImage(file="artist arsenal.png")
    label_imagem = Label(janela, image=img)
    label_imagem.pack()
    botoes_menu()
    janela.mainloop()

def tela_voltar_cadastro() :
    global janela
    janela.destroy()
    janela = Tk()
    janela.title("                                                                          Menu Principal")
    janela.config(background="#49A")
    janela.geometry("700x550")
    janela.maxsize(width=900, height=700)

    Label(janela,text="MENU").pack()
    img = PhotoImage(file="artist arsenal.png")
    label_imagem = Label(janela, image=img)
    label_imagem.pack()
    botoes_menu()
    janela.mainloop()

def tela_cadastrar_artista():
    global janela
    janela.destroy()
    janela = Tk()
    janela.title("Cadastro De Artistas")
    janela.geometry("650x550")
    janela.maxsize(width=900, height=700)
    janela.config(background="#49A")
    Label(janela, text="CADASTRO", bg="white", font="Moonrocks", width=50).place(x=0, y=50, width=700, height=80)
    Label(janela, text="Nome do album:", background="white", font="Moonrocks", width=25).place(x=40, y=150)
    global Nome_album
    Nome_album = Entry(janela, width=38)
    Nome_album.place(x=40, y=190)
    Label(janela, text="Nome da banda/artista:", background="white", font="Linotype", width=25).place(x=390,
                                                                                                               y=150)
    global Nome_artista
    Nome_artista = Entry(janela, width=38)
    Nome_artista.place(x=390, y=190)

    Label(janela, text="Data de lancamento do album:", background="white", font="Linotype", width=25).place(x=390, y=230)
    global Data_artista
    Data_artista = Entry(janela, width=38)
    Data_artista.place(x=390, y=270)

    lista_combobox = ["Sim", "Não"]
    Label(janela, text="foi o ultimo album lançado?", background="white", font="Linotype", width=25).place(x=50, y=230)
    global combobox_album
    combobox_album = ttk.Combobox(janela, values=lista_combobox, width=38)
    combobox_album.place(x=30, y=260)
    botao_enviar = Button(janela, text="Enviar Dados", command=lambda: domain.dados_artista(Nome_album,Nome_artista,Data_artista,combobox_album), font="Linotype", activebackground="blue",width=30)
    botao_enviar.place(x=50, y=500)
    botao("Voltar Menu",x=345, y=500,acao=tela_voltar_cadastro)
    janela.mainloop()

def sucesso():
    global janela
    janela.destroy()
    janela = Tk()
    janela.title("Sucesso")
    janela.geometry("650x550")
    janela.maxsize(width=900, height=700)
    janela.config(background="#49A")
    Label(janela, text="SUCESSO", bg="white", font="Moonrocks", width=50).place(x=0, y=50, width=700, height=80)
    botao("Voltar", x=345, y=500, acao=tela_cadastrar_artista)
    janela.mainloop()

def erro():
    global janela
    janela.destroy()
    janela = Tk()
    janela.title("Erro")
    janela.geometry("650x550")
    janela.maxsize(width=900, height=700)
    janela.config(background="#49A")
    Label(janela, text="CAMPO VAZIO", bg="white", font="Moonrocks", width=50).place(x=0, y=50, width=700, height=80)
    botao("Voltar", x=345, y=500, acao=tela_cadastrar_artista)
    janela.mainloop()
