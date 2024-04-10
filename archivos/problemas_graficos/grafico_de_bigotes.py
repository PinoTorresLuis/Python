import pandas as pd
#MatplotLib una libreria de visualización de datos
import matplotlib.pyplot as plt
#Seaborn una libreria de gráficos estadisticos
import seaborn as sns

df = pd.read_csv("archivos\\problemas_graficos\\grafico_bigotes.csv")
#Creando un gráfico de cuartiles
sns.boxplot(x="categoria", y="valor",data=df) # con data = df le estoy diciendo donde tiene que buscar esa columna

#Muestra la distribución de datos en quartiles, básicamente resaltando el promedio y los valores atípicos.

plt.show() #Mostramos el grafico