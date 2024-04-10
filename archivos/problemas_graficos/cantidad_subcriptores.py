import pandas as pd
#MatplotLib una libreria de visualización de datos
import matplotlib.pyplot as plt
#Seaborn una libreria de gráficos estadisticos
import seaborn as sns

df = pd.read_csv("archivos\\problemas_graficos\\cantidad_sub.csv")
#Creando un gráfico de lineas
sns.lineplot(x="fecha", y="subs",data=df) # con data = df le estoy diciendo donde tiene que buscar esa columna

plt.plot("01-06",20,"o")
plt.show()