





class Impresiones():
    
    def __init__(self,color, numero, cantidad):
        self.color = color
        self.numero = numero
        self.cantidad = cantidad
        
    def imprimir(self):
        print(self.color,self.numero,self.cantidad)
        



class Impresion2(Impresiones):
    def __init__(self,color,numero,cantidad,tamano):
        super().__init__(color,numero,cantidad)
        
        self.cantidad = tamano
        
        
    
        
            

Impresion = Impresion2("amarillo",34,45,"34cm")



Impresion.imprimir()


    