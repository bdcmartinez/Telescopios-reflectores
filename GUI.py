from msilib.schema import ComboBox
import sys
from turtle import settiltangle 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget

class Window(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI.app.ui",self)
        
        
        self.Boton_luz.setEnabled(False)
        self.Boton_imprimir.clicked.connect(self.fn_imprimir)
        
        self.Boton_borrar.clicked.connect(self.fn_Borrar_datos)
        self.Boton_luz.clicked.connect(self.fn_Animacion_luz)
    

    
    def fn_Borrar_datos(self):
        self.LineEdit_limites.setText("")
        self.LineEdit_Foco.setText("")
        self.LineEdit_Vertice.setText("")
        self.LineEdit_a.setText("")
        self.LineEdit_b.setText("")
        
        print("Funcionando borrar datos")
        
    def fn_imprimir(self):   
        demo.show()
        print("Funcionando Imprimir")
        
    def fn_Animacion_luz(self):
        print("Funcionando luz")
 

class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(4.5, 3.5), dpi=150)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)
        
        self.ax.plot(t, s)

        self.ax.set(xlabel='time (s)', ylabel='voltage (mV)',
               title='About as simple as it gets, folks')
        self.ax.grid()

class AppDemo(QWidget)      :
    def __init__(self):
        super().__init__()
        self.resize(650, 535)

        chart = Canvas(self)


        
if __name__ == '__main__':
    app=QApplication(sys.argv)
    GUI = Window()
    demo = AppDemo()
    GUI.show() 
    sys.exit(app.exec_())