from msilib.schema import ComboBox
import sys
from turtle import settiltangle 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
from sympy import C

"""

class parabola_horizontal():
    def __init__(self, foco, vertice, limits, X):
        self.limits = limits
        self.foco = foco
        self.vertice = vertice
        self.X = X

    def plot_parabola_horizontal(self):
        lim_x_i, lim_x_f = self.limits[0]
        lim_y_i, lim_y_f = self.limits[1]
        Y_plus  = []
        Y_minus = []
        for x in self.X :
            y_plus  = + (4*self.foco*(x-self.vertice[0]))**(0.5) + self.vertice[1]
            y_minus = - (4*self.foco*(x-self.vertice[0]))**(0.5) + self.vertice[1]
            Y_plus = np.append(Y_plus, [y_plus]) 
            Y_minus = np.append(Y_minus, [y_minus]) 
        plt.xlim(lim_x_i, lim_x_f)
        plt.ylim(lim_y_i, lim_y_f)
        plt.plot(self.X, Y_plus, c='b')
        plt.plot(self.X, Y_minus, c='b')
        plt.scatter(self.vertice[0] + self.foco , self.vertice[1], c='r')
        plt.xticks([self.vertice[0]], ['f'] )
        plt.yticks([], [] )
        plt.title('PARÁBOLA HORIZONTAL')
        plt.show()

class Elipse_horizontal():
    def __init__(self, a, b, centro,X, limits):
        self.limits = limits
        self.a = a
        self.b = b
        self.centro = centro
        self.c = (self.a**2 - self.b**2 )**(0.5)
        self.X = X
    def plot_elipse_horizontal(self):
        lim_x_i, lim_x_f = self.limits[0]
        lim_y_i, lim_y_f = self.limits[1]
        Y_plus = []
        Y_minus = []
        for x in self.X:
            y_plus  = self.centro[1] + self.b * ( 1 - ( (x - self.centro[0] )**2 / ( self.a**2 ) ) )**(0.5)
            y_minus = self.centro[1] - self.b * ( 1 - ( (x - self.centro[0] )**2 / ( self.a**2 ) ) )**(0.5)
            Y_plus = np.append(Y_plus, [y_plus])
            Y_minus = np.append(Y_minus, [y_minus])
        plt.xlim(lim_x_i, lim_x_f)
        plt.ylim(lim_y_i, lim_y_f)
        plt.plot(self.X, Y_plus, c='b')
        plt.plot(self.X, Y_minus, c='b')
        plt.scatter(self.centro[0] - self.c , self.centro[1], c='r')
        plt.scatter(self.centro[0] + self.c , self.centro[1], c='r')
        plt.xticks([self.centro[0] - self.c, self.centro[0] + self.c], ['f', 'f'] )
        plt.yticks([], [] )
        plt.title('ÉLIPSE')
        plt.show()

class Hiperbola_horizontal():
    
    
    def __init__(self, a, b, centro, X, limits):
        self.limits = limits
        self.a = a
        self.b = b
        self.centro = centro
        self.X = X
        self.c = (self.a**2 + self.b**2 )**(0.5)

    def plot_hiperbola_horizontal(self):
        lim_x_i, lim_x_f = self.limits[0]
        lim_y_i, lim_y_f = self.limits[1]
        Y_plus = []
        Y_minus = []
        for x in self.X :
            y_plus  = self.centro[0] + self.a * ( 1 + ( (x - self.centro[1] )**2 / ( self.b**2 ) ) )**(0.5)
            y_minus = self.centro[0] - self.a * ( 1 + ( (x - self.centro[1] )**2 / ( self.b**2 ) ) )**(0.5)
            Y_plus = np.append(Y_plus, [y_plus])
            Y_minus = np.append(Y_minus, [y_minus])
        plt.xlim(lim_x_i, lim_x_f)
        plt.ylim(lim_y_i, lim_y_f)
        plt.plot(Y_plus, self.X, c='b')
        plt.plot(Y_minus, self.X, c='b')
        plt.scatter(self.centro[0] - self.a , self.centro[1] , c='b')
        plt.scatter(self.centro[0] + self.a, self.centro[1]  , c='b')
        plt.scatter(self.centro[0] - self.c , self.centro[1] , c='r')
        plt.scatter(self.centro[0] + self.c, self.centro[1]  , c='r')
        plt.xticks([self.centro[0]], ['f'] )
        plt.yticks([], [] )
        plt.title('HIPÉRBOLA')
        plt.show()

"""


class parabola_horizontal():
    def __init__(self, foco, vertice, limits, X,nombre):
        self.limits = limits
        self.foco = foco
        self.vertice = vertice
        self.X = X
        self.nombre = nombre

    def plot_parabola_horizontal(self):
        lim_x_i, lim_x_f = self.limits[0]
        lim_y_i, lim_y_f = self.limits[1]
        Y_plus  = []
        Y_minus = []
        for x in self.X :
            y_plus  = + (4*self.foco*(x-self.vertice[0]))**(0.5) + self.vertice[1]
            y_minus = - (4*self.foco*(x-self.vertice[0]))**(0.5) + self.vertice[1]
            Y_plus = np.append(Y_plus, [y_plus]) 
            Y_minus = np.append(Y_minus, [y_minus]) 
        plt.xlim(lim_x_i, lim_x_f)
        plt.ylim(lim_y_i, lim_y_f)
        plt.plot(self.X, Y_plus, c='b')
        plt.plot(self.X, Y_minus, c='b')
        plt.scatter(self.vertice[0] + self.foco , self.vertice[1], c='r')
        plt.xticks([self.vertice[0]], ['f'] )
        plt.yticks([], [] )
        plt.title("TELESCOPIO "+self.nombre)
        plt.show()

class Elipse_horizontal():
    def __init__(self, a, b, centro,X, limits):
        self.limits = limits
        self.a = a
        self.b = b
        self.centro = centro
        self.c = (self.a**2 - self.b**2 )**(0.5)
        self.X = X
    def plot_elipse_horizontal(self):
        lim_x_i, lim_x_f = self.limits[0]
        lim_y_i, lim_y_f = self.limits[1]
        Y_plus = []
        Y_minus = []
        for x in self.X:
            y_plus  = self.centro[1] + self.b * ( 1 - ( (x - self.centro[0] )**2 / ( self.a**2 ) ) )**(0.5)
            y_minus = self.centro[1] - self.b * ( 1 - ( (x - self.centro[0] )**2 / ( self.a**2 ) ) )**(0.5)
            Y_plus = np.append(Y_plus, [y_plus])
            Y_minus = np.append(Y_minus, [y_minus])
        plt.xlim(lim_x_i, lim_x_f)
        plt.ylim(lim_y_i, lim_y_f)
        plt.plot(self.X, Y_plus, c='b')
        plt.plot(self.X, Y_minus, c='b')
        plt.scatter(self.centro[0] - self.c , self.centro[1], c='r')
        plt.scatter(self.centro[0] + self.c , self.centro[1], c='r')
        plt.xticks([self.centro[0] - self.c, self.centro[0] + self.c], ['f', 'f'] )
        plt.yticks([], [] )
        plt.show()

class Hiperbola_horizontal():
    
    
    def __init__(self, a, b, centro, X, limits):
        self.limits = limits
        self.a = a
        self.b = b
        self.centro = centro
        self.X = X
        self.c = (self.a**2 + self.b**2 )**(0.5)
        
    def plot_hiperbola_horizontal(self):
        lim_x_i, lim_x_f = self.limits[0]
        lim_y_i, lim_y_f = self.limits[1]
        Y_plus = []
        Y_minus = []
        for x in self.X :
            y_plus  = self.centro[0] + self.a * ( 1 + ( (x - self.centro[1] )**2 / ( self.b**2 ) ) )**(0.5)
            y_minus = self.centro[0] - self.a * ( 1 + ( (x - self.centro[1] )**2 / ( self.b**2 ) ) )**(0.5)
            Y_plus = np.append(Y_plus, [y_plus])
            Y_minus = np.append(Y_minus, [y_minus])
        plt.xlim(lim_x_i, lim_x_f)
        plt.ylim(lim_y_i, lim_y_f)
        plt.plot(Y_plus, self.X, c='b')
        #plt.plot(Y_minus, self.X, c='b')
        plt.scatter(self.centro[0] - self.a , self.centro[1] , c='b')
        plt.scatter(self.centro[0] + self.a, self.centro[1]  , c='b')
        plt.scatter(self.centro[0] - self.c , self.centro[1] , c='r')
        plt.scatter(self.centro[0] + self.c, self.centro[1]  , c='r')
        plt.xticks([self.centro[0]], ['f'] )
        plt.yticks([], [] )
        plt.show()



class Window(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI.app.ui",self)
        self.setWindowTitle("Telescopios")
        
        self.Label_a.setEnabled(False)
        self.Label_b.setEnabled(False)
        self.LineEdit_a.setEnabled(False)
        self.LineEdit_b.setEnabled(False)     
        
        self.Boton_imprimir.clicked.connect(self.fn_imprimir)
        
        self.Boton_borrar.clicked.connect(self.fn_Borrar_datos)
        #self.Boton_luz.clicked.connect(self.fn_Animacion_luz)
    
        self.ComboBox_Conicas.activated.connect(self.fn_Cambiar)  #Sirve para detectar que elemento esta en el combo box
        self.ComboBox_ConicaSelect.activated.connect(self.fn_CambiarBienvenida)
    
    def fn_CambiarBienvenida(self):
        self.Label_Bienvenida.setText("Inserte los datos de la " + self.ComboBox_ConicaSelect.currentText())
    def fn_Cambiar(self):
        
        self.Label_Conicas.setText("")

        if self.ComboBox_Conicas.currentText() != "Newtoniano":            
            self.LineEdit_Foco.setEnabled(False)
            self.Label_Foco.setEnabled(False)
            
            self.Label_a.setEnabled(True)
            self.Label_b.setEnabled(True)
            self.LineEdit_a.setEnabled(True)
            self.LineEdit_b.setEnabled(True)
        
        
        else:
            self.LineEdit_Foco.setEnabled(True)
            self.Label_Foco.setEnabled(True)       
            self.Label_a.setEnabled(False)
            self.Label_b.setEnabled(False)
            self.LineEdit_a.setEnabled(False)
            self.LineEdit_b.setEnabled(False)
            
        if self.ComboBox_Conicas.currentText() == "Newtoniano":
            self.ComboBox_ConicaSelect.clear()
            
            
            self.Label_Conicas.setText("Parábola")
            
            self.ComboBox_ConicaSelect.addItem("Parábola")
            
        if self.ComboBox_Conicas.currentText() == "Gregoriano":
            self.ComboBox_ConicaSelect.clear()
            
            self.Label_Conicas.setText("Elipse y Parábola")
            
            self.ComboBox_ConicaSelect.addItem("Parábola")
            self.ComboBox_ConicaSelect.addItem("Elipse")
            
            
        if self.ComboBox_Conicas.currentText() == "Cassegrain":
            self.ComboBox_ConicaSelect.clear()
            
            self.Label_Conicas.setText("Hipérbola y Parábola")
            
            self.ComboBox_ConicaSelect.addItem("Hiperbola")
            self.ComboBox_ConicaSelect.addItem("Parábola")
    
    


    def fn_Borrar_datos(self):
        self.LineEdit_Foco.setText("")
        self.LineEdit_VcoordenadaX.setText("")
        self.LineEdit_VcoordenadaY.setText("")
        self.LineEdit_a.setText("")
        self.LineEdit_b.setText("")


        print(self.ComboBox_Conicas.currentText())
        
        print("Funcionando borrar datos")
        
    def fn_imprimir(self):   
        
        demo = AppDemo()
        #demo.show()
        print("Funcionando Imprimir")
        
    def fn_Animacion_luz(self):
        print("Funcionando luz")
 

class Canvas(FigureCanvas):
    def __init__(self, parent):
        #fig, self.ax = plt.subplots(figsize=(4.5, 3.5), dpi=150)
        #super().__init__(fig)
        #self.setParent(parent)
        
        
        if GUI.ComboBox_Conicas.currentText() == "Newtoniano": #parabola
            
            
            y = float(GUI.LineEdit_VcoordenadaY.text())
            x = float(GUI.LineEdit_VcoordenadaX.text())
            f = float(GUI.LineEdit_Foco.text())
            
            X = np.linspace(x,x+f,200)
            limits = [[- (-15+x)  , -15+x], [- (-15+x) , -15+x]]
            centro = [x, y]

            
            parabola_1 = parabola_horizontal(f, centro, limits, X,"NEWTONIANO")
            parabola_1.plot_parabola_horizontal()      
            
                    
        if GUI.ComboBox_Conicas.currentText() == "Gregoriano": #Elipse

            y = float(GUI.LineEdit_VcoordenadaY.text())
            x = float(GUI.LineEdit_VcoordenadaX.text())
            
            a = float(GUI.LineEdit_a.text())
            b = float(GUI.LineEdit_b.text())
            X = np.linspace(x+3*a/4,x+a,200)
            limits = [[- (-15+x)  , -15+x], [- (-15+x) , -15+x]]
            centro = [x, y]

            
            elipse_1 = Elipse_horizontal(a, b, centro, X, limits)
            elipse_1.plot_elipse_horizontal()  
            
            
            
            c = np.sqrt(a**2-b**2)
            f = c
            
            X = np.linspace(x,x+f,200)
            limits = [[- (-15+x)  , -15+x], [- (-15+x) , -15+x]]
            centro = [x, y]

            
            parabola_1 = parabola_horizontal(f, centro, limits, X,"GREGORIANO")
            parabola_1.plot_parabola_horizontal()    
  
                                                  
        if GUI.ComboBox_Conicas.currentText() == "Cassegrain": #Hiperbola
                
            y = float(GUI.LineEdit_VcoordenadaY.text())
            x = float(GUI.LineEdit_VcoordenadaX.text())
            
            a = float(GUI.LineEdit_a.text())
            b = float(GUI.LineEdit_b.text())
            X = np.linspace(-6+y, 6+y,200)
            limits = [[- (-15+y)  , -15+y], [- (-15+y) , -15+y]]
            centro = [x, y]

            
            hiperbola_1 = Hiperbola_horizontal(a, b, centro, X, limits)
            hiperbola_1.plot_hiperbola_horizontal()        
        
            c = np.sqrt(a**2+b**2)
            f = c
            
            X = np.linspace(x,x+f,200)
            limits = [[- (-15+x)  , -15+x], [- (-15+x) , -15+x]]
            centro = [x, y]

            
            parabola_1 = parabola_horizontal(f, centro, limits, X,"CASSEGRAIN")
            parabola_1.plot_parabola_horizontal()      
                        
            


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(650, 535)

        chart = Canvas(self)


        
if __name__ == '__main__':
    app=QApplication(sys.argv)
    GUI = Window()
    GUI.show() 
    sys.exit(app.exec_())