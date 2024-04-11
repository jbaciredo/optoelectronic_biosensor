import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

###################################################################################################

list_columns = ['10^8cop_h', '75nM_h', '75nM', 'p18_h', 'vacio_1', 'vacio_2','AuNP', 'PBS', 'vacio_3', 'vacio_4', 'vacio_5', 'vacio_6', 'vacio_7', 'vacio_8','AuNP_2', 'PBS_2']
t_cicle = 3.2

#####################################################################################################

class Assay:
    def __init__(self, name, reads, aunp, target, c_nacl, temperature, media):
        
        self.name = name
        self.reads = reads
        self.aunp = aunp  
        self.target = target
        self.c_nacl = c_nacl
        self.temperature = temperature
        self.media = media
        self.data = pd.DataFrame(copy=True)  

    def add_data(self, reads):
        # CREAR UN DATA FRAME A PARTIR DE LOS ARCHIVOS DE LECTURA, LOS ORDENA Y ASIGNA NOMBRE A LAS COLUMNAS
        dfs = []
        for __ in range(int(reads)):
            dfs.append(pd.read_table("Lectura_"+str(__)+".txt", header = None, sep = ","))                      
        data = pd.concat(dfs, ignore_index = True)
        self.data = pd.concat([self.data, data], ignore_index=True)
        return self.data     #ESTO NO SE SI TENGO QUE PONER QUE SEA EL VALOR DE RETORNO DE LA FUNCION O NO 

    def sort_cols(self, target):        
        #El objetivo de esta funcion es ordenar las columnas y etiquetarlas de acuerdo a como se realizo el experimento
        df_sorted = self.data[[1, 0, 3, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 8, 15]]
        df_sorted.columns = target 
        self.data = df_sorted
        return self.data

    def graphs_vs_t(self, _):
        t_seg = np.arange(0, round((len(self.data))*(t_cicle), 2), t_cicle)   #en segundos
        t_hour = t_seg * (1/3600)
        self.data["Tiempo"]= t_hour 
        for column in self.data:
            if column != "Tiempo":
                plt.scatter(x=self.data["Tiempo"], y=self.data[column], color="crimson", s=0.2)
                plt.title(f"Light intensity vs Time {expto1.name}", loc = "center")
                plt.ylabel(f"Light Intensity raw {column}")
                plt.xlabel("Time (h)")
                plt.show()
            else:
                pass

expto1 = Assay("240131", 20, "MBN", list_columns, "0.3M", "RT", "PBS")
expto1.add_data(expto1.reads)
expto1.sort_cols(expto1.target)
expto1.graphs_vs_t(expto1)

