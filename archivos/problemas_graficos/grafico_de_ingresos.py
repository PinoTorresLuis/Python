import pandas as pd
#MatplotLib una libreria de visualización de datos
import matplotlib.pyplot as plt
#Seaborn una libreria de gráficos estadisticos
import seaborn as sns

df = pd.read_csv("archivos\\problemas_graficos\\ingresos_redes.csv")
#Creando un gráfico de barras
sns.barplot(x="fuentes", y="ingresos",data=df) # con data = df le estoy diciendo donde tiene que buscar esa columna

total_ingresos = df['ingresos'].sum() #pidiendo que sume los valoes de ingresos
print(f'La suma total de los ingresos del mes fueron : ${total_ingresos} USD')

plt.show() #Mostramos el grafico