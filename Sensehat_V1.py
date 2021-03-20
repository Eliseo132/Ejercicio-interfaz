#Programa Sensehat sin medición continua.
#Eliseo Villagrasa Guerrero.

import tkinter as tk
import tkinter.ttk as ttk
from sense_emu import SenseHat
import time 
import matplotlib.pyplot as plt 
import datetime

sense = SenseHat()

class Aplicacion:
    def __init__(self):
        self.contador_mediciones = 0
        self.contador_mediciones_guardadas = 0
        self.ventana = tk.Tk()
        self.ventana.title("Práctica SenseHat")
        self.cuaderno1 = ttk.Notebook(self.ventana, height = 800, width = 1000, padding = 10)
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text = "Monitorización")

        self.labelframe1 = ttk.LabelFrame(self.pagina1, text = "Control")        
        self.labelframe1.grid(column = 0, row = 2, padx = 5, pady = 10)        
        self.control()

        self.labelframe2 = ttk.LabelFrame(self.pagina1, text = "Medidas", height = 125, width = 650)        
        self.labelframe2.grid(column = 0, row = 3, padx = 5, pady = 10)  
        self.labelframe2.grid_propagate(False)      
        self.medidas()

        self.labelframe3 = ttk.LabelFrame(self.pagina1, padding = 30, text = "Histórico")  
        self.labelframe3.grid(column = 0, row = 4, padx = 5, pady = 10)        
        self.historico()

        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text = "Gráfica")

        self.cuaderno1.grid(column = 0, row = 0)     
        self.ventana.mainloop()


    def control(self):
        #Inicio pulsador 1.
        self.boton1 = ttk.Button(self.labelframe1, text = "Tomar datos", command = self.medir)
        self.boton1.grid(column = 1, row = 0, padx = 4, pady = 4)

        #Inicio label 1.
        self.label1 = ttk.Label(self.labelframe1, text = "Periodo: ")
        self.label1.grid(column = 0, row = 1, padx = 4, pady = 4)

        valor = 1
        #Inicio label 2.
        self.label2 = ttk.Label(self.labelframe1, text = valor)
        self.label2.grid(column = 1, row = 1, padx = 4, pady = 4)


    def medidas(self):
        #Salida de datos.
        #Datos seleccionados. 
        self.dato = tk.IntVar(value = 0)    
        self.labelSeleccionDatos = tk.Label(self.labelframe2, text = "Resultados elegidos:")
        self.labelSeleccionDatos.grid(column = 0, row = 0)         
        self.entry2 = ttk.Entry(self.labelframe2, textvariable = self.dato, justify = tk.CENTER)
        self.entry2.grid(column = 1, row = 0, padx = 4, pady = 4)
        

        #Datos no seleccionados.
        self.noSelect1 = tk.StringVar(value = "No seleccionado 1: ")
        self.noSelect2 = tk.StringVar(value = "No seleccionado 2: ")

        self.noSelect3 = tk.IntVar(value = 0)
        self.noSelect4 = tk.IntVar(value = 0)

        self.labelDatosNoSeleccionados1 = tk.Label(self.labelframe2, text = self.noSelect1.get())
        self.labelDatosNoSeleccionados1.grid(column = 2, row = 0)

        self.labelDatosNoSeleccionados2 = tk.Label(self.labelframe2, text = self.noSelect3.get())
        self.labelDatosNoSeleccionados2.grid(column = 3, row = 0)

        self.labelDatosNoSeleccionados3 = tk.Label(self.labelframe2, text = self.noSelect2.get())
        self.labelDatosNoSeleccionados3.grid(column = 2, row = 1)

        self.labelDatosNoSeleccionados4 = tk.Label(self.labelframe2, text = self.noSelect4.get())
        self.labelDatosNoSeleccionados4.grid(column = 3, row = 1)

        #Fecha de toma de datos.
        self.labelFechaMedicion = tk.Label(self.labelframe2, text = "Fecha de medición: ")
        self.labelFechaMedicion.grid(column = 2, row = 3)
        self.labelDatosFecha = tk.Label(self.labelframe2, text = datetime.datetime.now())
        self.labelDatosFecha.grid(column = 3, row = 3)
        
        #Inicio botones radio.
        self.seleccion = tk.IntVar()
        self.seleccion.set(2)

        self.radio1 = tk.Radiobutton(self.labelframe2,text = "Temperatura", variable = self.seleccion, value = 1)
        self.radio1.grid(column = 0, row = 4)
        self.radio2 = tk.Radiobutton(self.labelframe2,text = "Presión", variable = self.seleccion, value = 2)
        self.radio2.grid(column = 1, row = 4)
        self.radio3 = tk.Radiobutton(self.labelframe2,text = "Humedad", variable = self.seleccion, value = 3)
        self.radio3.grid(column = 2, row = 4)
    
    def historico(self):        
        #Inicio scrollbar.
        self.scroll1 = tk.Scrollbar(self.labelframe3, orient = tk.VERTICAL)
        self.tree = ttk.Treeview(self.labelframe3, yscrollcommand = self.scroll1.set)
        self.tree.grid(column = 0, columnspan = 3, row = 0)
        self.scroll1.configure(command = self.tree.yview) 
        self.scroll1.grid(column = 3, row = 0, sticky = 'NS')  
        self.tree['columns'] = ('Valor', 'Fecha/Hora', 'Tipo')

        self.tree.column('#0', anchor = tk.CENTER)
        self.tree.column('Valor', anchor = tk.CENTER)
        self.tree.column('Fecha/Hora', anchor = tk.CENTER)
        self.tree.column('Tipo', anchor = tk.CENTER)
  

        self.tree.heading('#0', text = 'Num')
        self.tree.heading('Valor', text = 'Valor')
        self.tree.heading('Fecha/Hora', text = 'Fecha/Hora')
        self.tree.heading('Tipo', text = 'Tipo')

        #Inicio botones.
        #Limpiar tabla.
        self.boton2 = ttk.Button(self.labelframe3, text = "Limpiar", command = self.borrar_datos)
        self.boton2.grid(column = 0, row = 1)

        #Calcular media.
        self.boton3 = ttk.Button(self.labelframe3, text = "Calcular media", command = self.calcular_media)
        self.boton3.grid(column = 1, row = 1)

        self.media = tk.IntVar(value = 0)

        self.mediaMediciones = tk.Label(self.labelframe3, text = "Media: ")
        self.mediaMediciones.grid(column = 0, row = 2)
        
        self.labelMediaMediciones = tk.Label(self.labelframe3, text = self.media.get())
        self.labelMediaMediciones.grid(column = 1, row = 2)

        #Exportar los datos.
        self.boton4 = ttk.Button(self.labelframe3, text = "Exportar")
        self.boton4.grid(column = 2, row = 1)

        #Inicio checkbox.
        self.seleccion1 = tk.IntVar()
        self.check1 = tk.Checkbutton(self.labelframe3, text = "Añadir a la lista", variable = self.seleccion1)
        self.check1.grid(column = 1, row = 3)
        
    
    def medir(self):      
        #Medidas redondeadas a 3 decimales.
        self.humedad = round(sense.humidity, 3)
        self.temp = round(sense.temperature, 3)
        self.pres = round(sense.pressure, 3)
        
        self.contador_mediciones += 1
        
        if self.seleccion.get() == 1:
            self.dato.set(self.temp) 
            self.labelDatosNoSeleccionados1.config(text = "Humedad: ")
            self.labelDatosNoSeleccionados3.config(text = "Presión: ")
            self.labelDatosNoSeleccionados2.config(text = self.humedad)
            self.labelDatosNoSeleccionados4.config(text = self.pres)
            self.labelDatosFecha.config(text = datetime.datetime.now())
            if self.seleccion1.get()== True:
                self.contador_mediciones_guardadas += 1
                self.tree.insert('', 0, text = self.contador_mediciones_guardadas, values = (self.temp, datetime.datetime.now(), 'Temperatura'))

        if self.seleccion.get() == 2:
            self.dato.set(self.pres)
            self.labelDatosNoSeleccionados1.config(text = "Humedad: ")
            self.labelDatosNoSeleccionados3.config(text = "Temperatura: ")
            self.labelDatosNoSeleccionados2.config(text = self.humedad)
            self.labelDatosNoSeleccionados4.config(text = self.temp)
            self.labelDatosFecha.config(text = datetime.datetime.now())
            if self.seleccion1.get()== True:
                self.contador_mediciones_guardadas += 1
                self.tree.insert('', 0, text = self.contador_mediciones_guardadas, values = (self.pres, datetime.datetime.now(), 'Presión'))

        if self.seleccion.get() == 3:
            self.dato.set(self.humedad)
            self.labelDatosNoSeleccionados1.config(text = "Temperatura: ")
            self.labelDatosNoSeleccionados3.config(text = "Presión: ")
            self.labelDatosNoSeleccionados2.config(text = self.temp)
            self.labelDatosNoSeleccionados4.config(text = self.pres)
            self.labelDatosFecha.config(text = datetime.datetime.now())    
            if self.seleccion1.get()== True:
                self.contador_mediciones_guardadas += 1
                self.tree.insert('', 0, text = self.contador_mediciones_guardadas, values = (self.humedad, datetime.datetime.now(), 'Humedad'))

    def borrar_datos(self):
        #Borra los datos de la lista.
        mediciones = self.tree.get_children()
        for medicion in mediciones:
            self.tree.delete(medicion)
        self.contador_mediciones_guardadas = 0
        self.media = 0
        self.labelMediaMediciones.config(text = self.media)

    def calcular_media(self): 
        #Calcula la media de los datos guardados.
        mediciones = self.tree.get_children()
        suma = 0
        for medicion in mediciones: 
            data = float(self.tree.item(medicion)["values"][0]) 
            suma += data
        self.media = (suma/self.contador_mediciones_guardadas)
        self.labelMediaMediciones.config(text = self.media)

aplicacion1 = Aplicacion()
