from tkinter import *
from tkinter import ttk, messagebox
import os

janela = Tk()


# funcao que será main e chamara as demais
def principal() :

    janela.mainloop()


##primeira tela a ser exibida
def exibicao() :
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
    botoes()
    janela.mainloop()


# tela de sera contruida quando usuario apertar em voltar
def tela_voltar_cadastro() :
    global janela
    janela = Tk()
    sair_janela_cadastro()
    janela.title("                                                                          Menu Principal")
    janela.config(background="#49A")
    janela.geometry("700x550")
    janela.maxsize(width=900, height=700)

    Label(janela,text="MENU").pack()
    botoes()
    janela.mainloop()

def tela_voltar_menu() :
    global janela
    janela = Tk()
    sair_busca()
    janela.title("                                                                          Menu Principal")
    janela.config(background="#49A")
    janela.geometry("700x550")
    janela.maxsize(width=900, height=700)
    botoes()
    janela.mainloop()

def sair() :
    global janela
    janela.destroy()


def sair_janela_cadastro() :
    global sair_janela_cadastro
    janela_cadastro.destroy()

def sair_busca():
    global sair_busca
    janela_busca.destroy()

def sair_listagem():
    global  sair_busca
    janela_busca_nome.destroy()
def dados() :
    if Nome_album.get() == "" or Nome_artista.get() == "" or Data_artista.get() == "" or combobox_album.get() == "" :
        messagebox.showinfo("AVISO", "dados não enviados")


    else :
        Label(janela_cadastro, text="Dados Enviados", background="green", width=30).place(x=270, y=330)
        with open("nomes.txt", "a", encoding="utf-8") as file :
            file.write(
                f"nome do album: {Nome_album.get()}| nome do artista: {Nome_artista.get()}| data de lancamento do album: {Data_artista.get()}| ultimo album lançado: {combobox_album.get()}|\n")
            Nome_album.delete(0, END)
            Nome_artista.delete(0, END)
            Data_artista.delete(0, END)
            combobox_album.set("")


def cadastrar_artista() :
    global janela_cadastro
    pastaApp = os.path.dirname(__file__)
    janela_cadastro = Tk()
    janela_cadastro.title("Cadastro De Artistas")
    janela_cadastro.geometry("650x550")
    janela.maxsize(width=900, height=700)
    janela_cadastro.config(background="#49A")
    cad = Label(janela_cadastro,text="CADASTRO", bg="white", font="Moonrocks",width=50)
    cad.place(x=0,y =50,width=700,height=80)
    Label(janela_cadastro, text="Nome do album:", background="white",font="Moonrocks",  width=25).place(x=40, y=150)
    global Nome_album
    Nome_album = Entry(janela_cadastro, width=38)
    Nome_album.place(x=40, y=190)

    Label(janela_cadastro, text="Nome da banda/artista:", background="white",font="Linotype", width=25).place(x=390, y=150)
    global Nome_artista
    Nome_artista = Entry(janela_cadastro, width=38)
    Nome_artista.place(x=390, y=190)

    Label(janela_cadastro, text="Data de lancamento do album:", background="white", font="Linotype", width=25).place(x=390, y=230)
    global Data_artista
    Data_artista = Entry(janela_cadastro, width=38)
    Data_artista.place(x=390, y=270)

    lista_combobox = ["Sim", "Não"]
    Label(janela_cadastro, text="foi o ultimo album lançado?", background="white", font="Linotype",width=25).place(x=50, y=230)
    global combobox_album
    combobox_album = ttk.Combobox(janela_cadastro, values=lista_combobox, width=38)
    combobox_album.place(x=30, y=260)
    botao = Button(janela_cadastro, text="Enviar Dados", command=dados, font="Linotype",activebackground="blue",width=30)
    botao.place(x=50, y=500)
    botaoSair = Button(janela_cadastro,text="Voltar Menu",  font="Linotype", activebackground="blue", command=tela_voltar_cadastro,width=30)
    botaoSair.place(x=345, y=500)
    sair()
    janela_cadastro.mainloop()


def buscar_artista() :
    sair()
    global janela_busca, Nome_usuario
    janela_busca = Tk()
    janela_busca.title("                                                                          Buscar Artistas")
    janela_busca.config(background="lightblue")
    janela_busca.geometry("700x550")
    janela_busca.maxsize(width=900, height=700)
    Label(janela_busca, text="Pesquisa por nome banda/artista:", activebackground="blue", width=25).place(x=50, y=50)

    Nome_usuario = Entry(janela_busca, width=30)
    Nome_usuario.place(x=50, y=80)
    botao_pesquisar_nome = Button(janela_busca, text="Pesquisar", command=pesquisar_nome)
    botao_pesquisar_nome.place(x=50, y=120)


    global v0
    v0 = IntVar()
    Label(janela_busca, text="Pesquisa por ano:", activebackground="blue", width=25).place(x=270, y=50)
    anterior = Radiobutton(janela_busca, text="Anterior", variable=v0, value=1)
    igual = Radiobutton(janela_busca, text="Igual", variable=v0, value=2)
    posterior = Radiobutton(janela_busca, text="Posterior",variable=v0, value=3)
    anterior.place(x=270,y=80)
    igual.place(x=270,y=110)
    posterior.place(x=270,y=140)
    botaoSair = Button(janela_busca, text="Voltar menu", activebackground="blue", command=tela_voltar_menu)
    botaoSair.place(x=270, y=410)
    global lista_combobox_ano
    with open("nomes.txt", "r", encoding="utf-8") as file :
        lista_combobox_ano = []
        for x in file.readlines() :
            lista_ano = []
            separador = x.split("|")
            lista_ano.append(separador[2])
            lista_ano = "".join(lista_ano)
            if lista_ano[30:] in lista_combobox_ano:
                pass
            else:
                lista_combobox_ano.append(lista_ano[30:])

    global combobox_ano

    combobox_ano = ttk.Combobox(janela_busca, values=lista_combobox_ano, width=25)
    combobox_ano.place(x=270, y=180)
    botao_pesquisar_data = Button(janela_busca, text="Pesquisar data",command=pesquisar_data)
    botao_pesquisar_data.place(x=270,y=220)




    janela_busca.mainloop()


def pesquisar_nome() :
    janela_busca_nome = Tk()
    janela_busca_nome.title(
        "                                                                          Lista resultado")
    janela_busca_nome.config(background="lightblue")
    janela_busca_nome.geometry("900x900")
    janela_busca_nome.maxsize(width=900, height=900)
    with open("nomes.txt", "r", encoding="utf-8") as file :
        variavel_mudanca = 0
        for x in file.readlines() :
            lista_album = []
            lista_nome = []
            lista_ano = []
            lista_ultimo_album = []
            separador = x.split("|")

            lista_album.append(separador [0])
            lista_nome.append(separador [1])
            lista_ano.append(separador [2])
            lista_ultimo_album.append(separador [3])

            lista_album = "".join(lista_album)
            lista_nome = "".join(lista_nome)
            lista_ano = "".join(lista_ano)
            lista_ultimo_album = "".join(lista_ultimo_album)
            if Nome_usuario.get().lower() in lista_nome [18:].lower() and Nome_usuario.get() != "" :
                Label(janela_busca_nome, text="Album", width=33, background="white").place(x=0, y=0)
                Label(janela_busca_nome, text="Nome artista/banda", width=33, background="white").place(x=225, y=0)
                Label(janela_busca_nome, text="Ano de lancamento", width=33, background="white").place(x=450, y=0)
                Label(janela_busca_nome, text="Ultimo album lancado", width=33, background="white").place(x=675, y=0)
                Label(janela_busca_nome, text=f"{lista_album.title()}", width=33, background="white").place(x=0,
                                                                                                            y=20 + variavel_mudanca)
                Label(janela_busca_nome, text=f"{lista_nome.title()}", width=33, background="white").place(x=225,
                                                                                                           y=20 + variavel_mudanca)
                Label(janela_busca_nome, text=f"{lista_ano.title()}", width=33, background="white").place(x=450,
                                                                                                          y=20 + variavel_mudanca)
                Label(janela_busca_nome, text=f"{lista_ultimo_album.title()}", width=33, background="white").place(
                    x=675, y=20 + variavel_mudanca)
                variavel_mudanca += 20
    janela_busca.destroy()

    janela_busca_nome.mainloop()

def pesquisar_data():
    if v0.get()==1:
        janela_busca_nome = Tk()
        janela_busca_nome.title(
            "                                                                          Lista resultado")
        janela_busca_nome.config(background="lightblue")
        janela_busca_nome.geometry("900x900")
        janela_busca_nome.maxsize(width=900, height=900)
        with open("nomes.txt", "r", encoding="utf-8") as file :
            variavel_mudanca = 0
            for x in file.readlines() :
                lista_album = []
                lista_nome = []
                lista_ano = []
                lista_ultimo_album = []
                separador = x.split("|")

                lista_album.append(separador [0])
                lista_nome.append(separador [1])
                lista_ano.append(separador [2])
                lista_ultimo_album.append(separador [3])

                lista_album = "".join(lista_album)
                lista_nome = "".join(lista_nome)
                lista_ano = "".join(lista_ano)
                lista_ultimo_album = "".join(lista_ultimo_album)
                if lista_ano[30:] <= combobox_ano.get():
                    Label(janela_busca_nome, text="Album", width=33, background="white").place(x=0, y=0)
                    Label(janela_busca_nome, text="Nome artista/banda", width=33, background="white").place(x=225, y=0)
                    Label(janela_busca_nome, text="Ano de lancamento", width=33, background="white").place(x=450, y=0)
                    Label(janela_busca_nome, text="Ultimo album lancado", width=33, background="white").place(x=675,
                                                                                                              y=0)
                    Label(janela_busca_nome, text=f"{lista_album.title()}", width=33, background="white").place(x=0,
                                                                                                                y=20 + variavel_mudanca)
                    Label(janela_busca_nome, text=f"{lista_nome.title()}", width=33, background="white").place(x=225,
                                                                                                               y=20 + variavel_mudanca)
                    Label(janela_busca_nome, text=f"{lista_ano.title()}", width=33, background="white").place(x=450,
                                                                                                              y=20 + variavel_mudanca)
                    Label(janela_busca_nome, text=f"{lista_ultimo_album.title()}", width=33, background="white").place(
                        x=675, y=20 + variavel_mudanca)
                    variavel_mudanca += 20
        janela_busca.destroy()
        janela_busca_nome.mainloop()

    elif v0.get()==2:
        janela_busca_nome = Tk()
        janela_busca_nome.title(
            "                                                                          Lista resultado")
        janela_busca_nome.config(background="lightblue")
        janela_busca_nome.geometry("900x900")
        janela_busca_nome.maxsize(width=900, height=900)
        with open("nomes.txt", "r", encoding="utf-8") as file :
            variavel_mudanca = 0
            for x in file.readlines() :
                lista_album = []
                lista_nome = []
                lista_ano = []
                lista_ultimo_album = []
                separador = x.split("|")

                lista_album.append(separador [0])
                lista_nome.append(separador [1])
                lista_ano.append(separador [2])
                lista_ultimo_album.append(separador [3])

                lista_album = "".join(lista_album)
                lista_nome = "".join(lista_nome)
                lista_ano = "".join(lista_ano)
                lista_ultimo_album = "".join(lista_ultimo_album)
                if lista_ano[30:] == combobox_ano.get():
                    Label(janela_busca_nome, text="Album", width=33, background="white").place(x=0, y=0)
                    Label(janela_busca_nome, text="Nome artista/banda", width=33, background="white").place(x=225, y=0)
                    Label(janela_busca_nome, text="Ano de lancamento", width=33, background="white").place(x=450, y=0)
                    Label(janela_busca_nome, text="Ultimo album lancado", width=33, background="white").place(x=675,
                                                                                                              y=0)
                    Label(janela_busca_nome, text=f"{lista_album.title()}", width=33, background="white").place(x=0,
                                                                                                                y=20 + variavel_mudanca)
                    Label(janela_busca_nome, text=f"{lista_nome.title()}", width=33, background="white").place(x=225,
                                                                                                               y=20 + variavel_mudanca)
                    Label(janela_busca_nome, text=f"{lista_ano.title()}", width=33, background="white").place(x=450,
                                                                                                              y=20 + variavel_mudanca)
                    Label(janela_busca_nome, text=f"{lista_ultimo_album.title()}", width=33, background="white").place(
                        x=675, y=20 + variavel_mudanca)
                    variavel_mudanca += 20

        janela_busca.destroy()
        janela_busca_nome.mainloop()

    elif v0.get()==3:
        janela_busca_nome = Tk()
        janela_busca_nome.title(
            "                                                                          Lista resultado")
        janela_busca_nome.config(background="lightblue")
        janela_busca_nome.geometry("900x900")
        janela_busca_nome.maxsize(width=900, height=900)
        with open("nomes.txt", "r", encoding="utf-8") as file :
            variavel_mudanca = 0
            for x in file.readlines() :
                lista_album = []
                lista_nome = []
                lista_ano = []
                lista_ultimo_album = []
                separador = x.split("|")

                lista_album.append(separador [0])
                lista_nome.append(separador [1])
                lista_ano.append(separador [2])
                lista_ultimo_album.append(separador [3])

                lista_album = "".join(lista_album)
                lista_nome = "".join(lista_nome)
                lista_ano = "".join(lista_ano)
                lista_ultimo_album = "".join(lista_ultimo_album)
                if lista_ano[30:] >= combobox_ano.get():
                    Label(janela_busca_nome, text="Album", width=33, background="white").place(x=0, y=0)
                    Label(janela_busca_nome, text="Nome artista/banda", width=33, background="white").place(x=225, y=0)
                    Label(janela_busca_nome, text="Ano de lancamento", width=33, background="white").place(x=450, y=0)
                    Label(janela_busca_nome, text="Ultimo album lancado", width=33, background="white").place(x=675,
                                                                                                              y=0)
                    Label(janela_busca_nome, text=f"{lista_album.title()}", width=33, background="white").place(x=0,
                                                                                                                y=20 + variavel_mudanca)
                    Label(janela_busca_nome, text=f"{lista_nome.title()}", width=33, background="white").place(x=225,
                                                                                                               y=20 + variavel_mudanca)
                    Label(janela_busca_nome, text=f"{lista_ano.title()}", width=33, background="white").place(x=450,
                                                                                                              y=20 + variavel_mudanca)
                    Label(janela_busca_nome, text=f"{lista_ultimo_album.title()}", width=33, background="white").place(
                        x=675, y=20 + variavel_mudanca)
                    variavel_mudanca += 20

        janela_busca.destroy()
        janela_busca_nome.mainloop()


def listagem() :
    global janela_busca_nome
    janela_busca_nome = Tk()
    sair()

    janela_busca_nome.title(
        "                                                                          Lista resultado")
    janela_busca_nome.config(background="lightblue")
    janela_busca_nome.geometry("900x900")
    janela_busca_nome.maxsize(width=900, height=900)
    with open("nomes.txt", "r", encoding="utf-8") as file :
        variavel_mudanca = 0
        for x in file.readlines() :
            lista_album = []
            lista_nome = []
            lista_ano = []
            lista_ultimo_album = []
            separador = x.split("|")

            lista_album.append(separador [0])
            lista_nome.append(separador [1])
            lista_ano.append(separador [2])
            lista_ultimo_album.append(separador [3])

            lista_album = "".join(lista_album)
            lista_nome = "".join(lista_nome)
            lista_ano = "".join(lista_ano)
            lista_ultimo_album = "".join(lista_ultimo_album)
            Label(janela_busca_nome, text="Album", width=33, background="white").place(x=0, y=0)
            Label(janela_busca_nome, text="Nome artista/banda", width=33, background="white").place(x=225, y=0)
            Label(janela_busca_nome, text="Ano de lancamento", width=33, background="white").place(x=450, y=0)
            Label(janela_busca_nome, text="Ultimo album lancado", width=33, background="white").place(x=675, y=0)
            Label(janela_busca_nome, text=f"{lista_album.title()}", width=33, background="white").place(x=0,
                                                                                                        y=20 + variavel_mudanca)
            Label(janela_busca_nome, text=f"{lista_nome.title()}", width=33, background="white").place(x=225,
                                                                                                       y=20 + variavel_mudanca)
            Label(janela_busca_nome, text=f"{lista_ano.title()}", width=33, background="white").place(x=450,
                                                                                                      y=20 + variavel_mudanca)
            Label(janela_busca_nome, text=f"{lista_ultimo_album.title()}", width=33, background="white").place(x=675,
                                                                                                               y=20 + variavel_mudanca)
            variavel_mudanca += 20

# botoes e label
def botoes() :
    global botaoCadastro, botaoListar
    botaoCadastro = Button(janela, text="Cadastrar Artista", activebackground="blue", bg="lightblue", width=50,
                           command=cadastrar_artista)
    botaoCadastro.place(x=170, y=330)
    botaoListar = Button(janela, text="Listagem", activebackground="blue", bg="lightblue", width=50, command=listagem)
    botaoListar.place(x=170, y=370)
    botaoBuscar = Button(janela, text="Buscar", activebackground="blue", bg="lightblue", width=50,
                         command=buscar_artista)
    botaoBuscar.place(x=170, y=410)
    botaoSair = Button(janela, text="Sair", activebackground="blue", bg="lightblue", width=50, command=sair)
    botaoSair.place(x=170, y=450)


exibicao()
