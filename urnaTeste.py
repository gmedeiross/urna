from tkinter import*

class Urna():
    def __init__(self):
        self.tela = Tk()
        self.tela.bind('<KeyPress>', self.teclado)
        self.tela.config(bg='black')
        self.tela.title('Vote')
        self.tela.iconbitmap('urna.ico')
        self.tela.geometry('500x300')
        self.tela.resizable(False, False)
        self.botoes()
        self.display()
        self.label()
        self.tela.mainloop()

    def botoes(self):
        self.aux = False
        self.aux2 = False
        self.valor = ''
        self.valor2 = ''
        self.text = StringVar()
        self.text2 = StringVar()

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

        confirmar = Button(self.tela, text="CONFIRMAR", font="Arial 9", bg='green')
        confirmar.place(x= 425, y=250, relwidth=0.15, relheight=0.13)

    def teclado(self, evento):
        lista = ['0','1','2','3','4','5','6','7','8','9']
        for i in lista:
            if i == evento.char:
                if self.aux == False:
                    self.valor = evento.char
                    self.text.set(self.valor)
                    self.aux = True

                elif self.aux2 == False:
                        self.valor2 = evento.char
                        self.text2.set(self.valor2)
                        self.aux2 = True



    def display(self):
        self.frame = Frame(self.tela)
        self.frame.place(x= 10, y= 15, relwidth=0.51, relheight=0.91)

        self.label1 = Label(self.tela, font="Arial 30", bg= '#DCDCDC', textvar=self.text, justify=CENTER)
        self.label1.place(relx=0.15, rely=0.30, relwidth=0.08, relheight=0.15)

        self.label2 = Label(self.tela, font="Arial 30", bg= '#DCDCDC', textvar=self.text2, justify=CENTER)
        self.label2.place(relx=0.24, rely=0.30, relwidth=0.08, relheight=0.15)

    def label(self):
        self.numero = Label(self.frame, text='Número:', font='Arial 10')
        self.numero.place(x=7, y=90)

        self.nome = Label(self.frame, text='Nome:', font='Arial 10')
        self.nome.place(x=7, y=150)


    def botoes_numerico(self, parametro):
        if self.aux == False:
            self.valor += parametro
            self.text.set(self.valor)
            self.aux = True

        elif self.aux2 == False:
            self.valor2 += parametro
            self.text2.set(self.valor2)
            self.aux2 = True


    def botao_corrige(self):
        if self.aux2 == True:
            self.valor2 = ''
            self.text2.set(self.valor2)
            self.aux2 = False
        
        elif self.aux == True:
            self.valor = ''
            self.text.set(self.valor)
            self.aux = False

Urna()