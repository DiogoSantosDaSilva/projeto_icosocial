from tkinter import *

ico = Tk()

# cor do background -> #8c2993 roxo

class Application():
    def __init__(self):
        self.ico = ico
        self.tela()
        ico.mainloop()
    def tela(self):
        self.ico.title('Cadastro de Alunos')
        self.ico.configure(background='#8c2993')
    

    

Application()
