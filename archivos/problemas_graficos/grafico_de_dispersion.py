import pandas as pd
#MatplotLib una libreria de visualización de datos
import matplotlib.pyplot as plt
#Seaborn una libreria de gráficos estadisticos
import seaborn as sns

df = pd.read_csv("archivos\\problemas_graficos\\grafico_dispersion.csv")
#Creando un gráfico de dispersion
sns.scatterplot(x="tiempo", y="dinero",data=df) # con data = df le estoy diciendo donde tiene que buscar esa columna

#El grafico que muestra es muy utilizado por IA y nos sirve para trazar distintos tipos de linea y poder predecir. También nos sirve para clasificar ya que nos arroja varios puntos entre las coordenadas

plt.show() #Mostramos el grafico