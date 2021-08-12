from tkinter import*

import mysql.connector



class Urna():

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(user = 'root', host='localhost')
            return self.conexao
        except:
            return False


    def usarBd(self):
        conexao = self.conectar()
        if conexao != False:
            try:
                print('erro')
            except:
                self.cursor.execute('USE urnabd;')
                conexao.close()
    

    def tabelaCandidato(self):
        conexao = self.conectar()
        if conexao != False:
            print('erro2')
    

    def confirmarVoto(self):
        valorDigitado = self.voto
        conexao = self.conectar()
        self.cursor = conexao.cursor()
        self.cursor.execute('USE urnabd;')

        if (valorDigitado == 22) or (valorDigitado == 39) or (valorDigitado == 64):
            self.cursor.execute(f"SELECT voto FROM candidato WHERE numero = {valorDigitado}")
            self.lista = self.cursor.fetchall()
            self.votos = self.lista[0]
            self.votos = self.votos[0] + 1
            self.cursor.execute(f"UPDATE candidato SET voto = {self.votos} WHERE numero = {valorDigitado}")
            self.conexao.commit()
            self.cursor.close()

    def __init__(self):
        self.tela = Tk()
        self.tela.bind('<KeyPress>', self.teclado)
        self.tela.config(bg='black')
        self.tela.title('Vote')
        self.tela.iconbitmap('urna.ico')
        self.tela.geometry('500x300')
        self.tela.resizable(False, False)
        self.tecladoNumerico()
        self.display()
        self.label()
        self.tela.mainloop()

    def tecladoNumerico(self):
        self.aux = False
        self.aux2 = False
        self.valor = ''
        self.valor2 = ''
        self.text = StringVar()
        self.text2 = StringVar()


        # Criação dos botões númeriocos da urna, para que seja possível o voto!
        numero = Button(self.tela, text="1", font="Arial 20", command=lambda:self.botoes_numerico('1'))
        numero.place(x= 275, y=50, relwidth=0.15, relheight=0.15)

        numero = Button(self.tela, text="2", font="Arial 20", command=lambda:self.botoes_numerico('2'))
        numero.place(x= 350, y=50, relwidth=0.15, relheight=0.15)

        numero = Button(self.tela, text="3", font="Arial 20", command=lambda:self.botoes_numerico('3'))
        numero.place(x= 425, y=50, relwidth=0.15, relheight=0.15)

        numero = Button(self.tela, text="4", font="Arial 20", command=lambda:self.botoes_numerico('4'))
        numero.place(x= 275, y=95, relwidth=0.15, relheight=0.15)

        numero = Button(self.tela, text="5", font="Arial 20", command=lambda:self.botoes_numerico('5'))
        numero.place(x= 350, y=95, relwidth=0.15, relheight=0.15)

        numero = Button(self.tela, text="6", font="Arial 20", command=lambda:self.botoes_numerico('6'))
        numero.place(x= 425, y=95, relwidth=0.15, relheight=0.15)

        numero = Button(self.tela, text="7", font="Arial 20", command=lambda:self.botoes_numerico('7'))
        numero.place(x= 275, y=140, relwidth=0.15, relheight=0.15)

        numero = Button(self.tela, text="8", font="Arial 20", command=lambda:self.botoes_numerico('8'))
        numero.place(x= 350, y=140, relwidth=0.15, relheight=0.15)

        numero = Button(self.tela, text="9", font="Arial 20", command=lambda:self.botoes_numerico('9'))
        numero.place(x= 425, y=140, relwidth=0.15, relheight=0.15)

        numero = Button(self.tela, text="0", font="Arial 20", command=lambda:self.botoes_numerico('0'))
        numero.place(x= 350, y=185, relwidth=0.15, relheight=0.15)

        branco = Button(self.tela, text="BRANCO", font="Arial 10")
        branco.place(x= 275, y=250, relwidth=0.15, relheight=0.13)

        corrige = Button(self.tela, text="CORRIGE", font="Arial 10", bg='red', command=lambda:self.botao_corrige())
        corrige.place(x= 350, y=250, relwidth=0.15, relheight=0.13)

        confirmar = Button(self.tela, text="CONFIRMAR", font="Arial 9", bg='green', command=lambda:self.confirmarVoto())
        confirmar.place(x= 425, y=250, relwidth=0.15, relheight=0.13)

    # função para conferir o número inserido pelo teclado e adicionando na label se for um número, conforme a lista a baixo.
    def teclado(self, evento):
        lista = ['0','1','2','3','4','5','6','7','8','9']   #lista q limita os botões que poderão ser ensiridos na label.
        for i in lista:
            if i == evento.char:                            
                if self.aux == False:                       #se 'aux' for False, isso indicara para o código q não há nem um número na label, permitindo que a tacla prescionada seja inserida na lab 
                    self.valor = evento.char
                    self.text.set(self.valor)               # faz a atualização da label com o valor inserido pelo usuário.
                    self.aux = True

                elif self.aux2 == False:                    # tem a mesma função que a de cima, mas, sendo aplicada na segunda label.
                        self.valor2 = evento.char
                        self.text2.set(self.valor2)
                        self.aux2 = True
            



    def display(self):
        self.frame = Frame(self.tela)
        self.frame.place(x= 10, y= 15, relwidth=0.51, relheight=0.91)

        self.label1 = Label(self.tela, font="Arial 30", bg= '#DCDCDC', textvar=self.text, justify=CENTER)       #cria o display do primeiro número.
        self.label1.place(relx=0.15, rely=0.30, relwidth=0.08, relheight=0.15)

        self.label2 = Label(self.tela, font="Arial 30", bg= '#DCDCDC', textvar=self.text2, justify=CENTER)      #cria o display do segundo número.
        self.label2.place(relx=0.24, rely=0.30, relwidth=0.08, relheight=0.15)

    def label(self):
        self.numero = Label(self.frame, text='Número:', font='Arial 10')
        self.numero.place(x=7, y=90)

        self.nome = Label(self.frame, text='Nome:', font='Arial 10')
        self.nome.place(x=7, y=150)

#__________________________Funções dos Botões______________________________

    def botoes_numerico(self, parametro):   #função que verifica se ah valor na primeira label(display), e insere se o valor for FALSE.
        if self.aux == False:
            self.valor += parametro
            self.text.set(self.valor)
            self.aux = True

        elif self.aux2 == False:            # se o resultado da anteriaor for True, ele faz a mesma coisa com a seguanda label(display) 
            self.valor2 += parametro
            self.text2.set(self.valor2)
            self.aux2 = True
        self.voto = int(self.valor + self.valor2)
        print(self.voto)
        self.mostra_nome()

    def mostra_nome(self):
        if self.voto == 22:
            self.nome3 = Label(self.frame, text='José Saramago', font='Arial 10')
            self.nome3.place(x=60, y=150)

        elif self.voto == 39:
            self.nome3 = Label(self.frame, text='Machado de Assis', font='Arial 10')
            self.nome3.place(x=60, y=150)

        elif self.voto == 64:
            self.nome3 = Label(self.frame, text='William Shakespeare', font='Arial 10')
            self.nome3.place(x=60, y=150)

    def botao_corrige(self):                # está função deleta/corrige, caso a pessoa queira mudar seu voto.
        if self.aux2 == True:
            self.valor2 = ''
            self.text2.set(self.valor2)
            self.aux2 = False

        elif self.aux == True:             
            self.valor = ''
            self.text.set(self.valor)
            self.aux = False



Urna()
