from tkinter import *
from tkinter import ttk, font
import getpass

class Aplicacion():
    def __init__(self):
        

        

        self.raiz = Tk()

        
        self.ancho = self.raiz.winfo_screenwidth()
        
        if self.ancho < 1001:
            self.multiplicador = 0.75
        elif self.ancho < 1501:
            self.multiplicador = 1
        elif self.ancho < 2001:
            self.multiplicador = 1.5
        elif self.ancho < 4001:
            self.multiplicador = 2
        else:
            self.multiplicador = 3
        print(self.multiplicador)
        
        cadena = str(int(600*self.multiplicador)) + 'x' + str(int(350*self.multiplicador)) + '+' + str(int((self.ancho/2)-((600*self.multiplicador)/2))) + '+' + str(int(50*self.multiplicador))
        print(cadena)
        self.raiz.geometry(cadena)
        
        self.raiz.configure(bg = 'gray90')
        self.raiz.resizable(0,0)
        self.raiz.title('GestorACOES')
        self.raiz.iconbitmap(default='myicon.ico')
        self.boton1 = ttk.Button(self.raiz, width = (int(10*self.multiplicador)), text="Exit", 
                                 padding=(int(5*self.multiplicador),int(5*self.multiplicador)), command=self.raiz.destroy)
        self.boton1.place(x=str(int(500*self.multiplicador)), y=str(int(275*self.multiplicador)))

        self.boton2 = ttk.Button(self.raiz, width = (int(10*self.multiplicador)), text="Log In", 
                                 padding=((int(5*self.multiplicador)),(int(5*self.multiplicador))), command=self.log_in)
        self.boton2.place(x=(int(400*self.multiplicador)), y=(int(275*self.multiplicador)))

        self.fuente = font.Font(weight='bold')                       
        self.etiq1 = ttk.Label(self.raiz, text="Usuario:", 
                               font=self.fuente)
        self.etiq2 = ttk.Label(self.raiz, text="Contraseña:", 
                               font=self.fuente)
        
         
        self.usuario = StringVar()
        self.clave = StringVar()

        self.ctext1 = ttk.Entry(self.raiz, 
                                textvariable=self.usuario, width=(int(80*self.multiplicador)))
        self.ctext2 = ttk.Entry(self.raiz, 
                                textvariable=self.clave, 
                                width=(int(80*self.multiplicador)),
                                show="*")
        self.ctext1.focus_set()
        self.ctext1.bind('<Return>',self.clave_in)
        self.ctext2.bind('<Button-1>',self.borrar_mensa)
        self.ctext2.bind('<Return>',self.log_in2)
        
        self.mensa = StringVar()
        self.mensa.set("Bienvenido a ACOES")
        self.bienvenida = ttk.Label(self.raiz, textvariable=self.mensa, 
                     font=self.fuente, foreground='SteelBlue1')
        self.bienvenida.config(font=("Times", (int(24*self.multiplicador)), "bold"))

        self.etiq1.place(x=(int(50*self.multiplicador)),y=(int(75*self.multiplicador)))
        self.ctext1.place(x=(int(50*self.multiplicador)),y=(int(110*self.multiplicador)))
        self.etiq2.place(x=(int(50*self.multiplicador)),y=(int(150*self.multiplicador)))
        self.ctext2.place(x=(int(50*self.multiplicador)),y=(int(185*self.multiplicador)))
        self.bienvenida.place(x=(int(150*self.multiplicador)),y=(int(25*self.multiplicador)))

        self.mensa2 = StringVar()
        self.mensa2.set("¿Ha olvidado su contraseña?")
        self.olvido = ttk.Label(self.raiz, textvariable=self.mensa2, 
                     font=self.fuente, foreground='SteelBlue1')
        self.olvido.config(font=("Times", (int(12*self.multiplicador)), "italic"))
        self.olvido.place(x=(int(340*self.multiplicador)),y=(int(225*self.multiplicador)))
        
        self.olvido.bind('<Button-1>',self.recuperar_contraseña)

        self.raiz.mainloop()

    def recuperar_contraseña(self, evento):
        self.bienvenida.configure(foreground='red')
        self.bienvenida.place(x=(int(75*self.multiplicador)),y=(int(25*self.multiplicador)))
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