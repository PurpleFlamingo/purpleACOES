from tkinter import *
from tkinter import ttk, font
import getpass

class Aplicacion():
    def __init__(self):
        
        self.raiz = Tk()
        self.raiz.geometry('600x350+500+50')
        self.raiz.configure(bg = 'gray90')
        self.raiz.resizable(0,0)
        self.raiz.title('GestorACOES')
        self.raiz.iconbitmap(default='myicon.ico')
        self.boton1 = ttk.Button(self.raiz, text="Exit", 
                                 padding=(5,5), command=self.raiz.destroy)
        self.boton1.place(x=500, y=275)
        
        
        self.boton2 = ttk.Button(self.raiz, text="Log In", 
                                 padding=(5,5), command=self.log_in)

        self.boton2.place(x=400, y=275)

        self.fuente = font.Font(weight='bold')                       
        self.etiq1 = ttk.Label(self.raiz, text="Usuario:", 
                               font=self.fuente)
        self.etiq2 = ttk.Label(self.raiz, text="Contraseña:", 
                               font=self.fuente)
        
         
        self.usuario = StringVar()
        self.clave = StringVar()

        self.ctext1 = ttk.Entry(self.raiz, 
                                textvariable=self.usuario, width=80)
        self.ctext2 = ttk.Entry(self.raiz, 
                                textvariable=self.clave, 
                                width=80,
                                show="*")
        self.ctext1.focus_set()
        self.ctext1.bind('<Return>',self.clave_in)
        self.ctext2.bind('<Button-1>',self.borrar_mensa)
        self.ctext2.bind('<Return>',self.log_in2)
        
        self.mensa = StringVar()
        self.mensa.set("Bienvenido a ACOES")
        self.bienvenida = ttk.Label(self.raiz, textvariable=self.mensa, 
                     font=self.fuente, foreground='SteelBlue1')
        self.bienvenida.config(font=("Times", 24, "bold"))

        self.etiq1.place(x=50,y=75)
        self.ctext1.place(x=50,y=110)
        self.etiq2.place(x=50,y=150)
        self.ctext2.place(x=50,y=185)
        self.bienvenida.place(x=150,y=25)

        self.mensa2 = StringVar()
        self.mensa2.set("¿Ha olvidado su contraseña?")
        self.olvido = ttk.Label(self.raiz, textvariable=self.mensa2, 
                     font=self.fuente, foreground='SteelBlue1')
        self.olvido.config(font=("Times", 12, "italic"))
        self.olvido.place(x=340,y=225)
        
        self.olvido.bind('<Button-1>',self.recuperar_contraseña)

        self.raiz.mainloop()

    def recuperar_contraseña(self, evento):
        self.bienvenida.configure(foreground='red')
        self.bienvenida.place(x=75,y=25)
        self.mensa.set("La contraseña es 1234")

    def clave_in(self, evento):
        self.ctext2.focus_set()

    def log_in2(self, evento):
        self.log_in()

    def log_in(self):
        if self.clave.get() == '1234':
            self.bienvenida.configure(foreground='blue')
            self.mensa.set("Welcome")            
        else:
            self.bienvenida.configure(foreground='red')
            self.mensa.set("You shall not pass")

    def borrar_mensa(self, evento):
        self.clave.set("")
        

def main():
    mi_app = Aplicacion()
    return 0


if __name__ == '__main__':
    main()