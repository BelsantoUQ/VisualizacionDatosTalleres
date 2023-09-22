
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carga el dataset
titanic = pd.read_csv("C:/Users/USER/Documents/Programacion/python/VisualizacionDatos/VisualizacionDatosTalleres/PEC 1/titanic.csv")

# Identifica las columnas con valores nulos
print(titanic.isnull().sum())


# Elimina columnas innecesarias
datos = titanic.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)

#Cantidad de pasajeros que sobrevivieron y murieron:
survival_counts = datos['Survived'].value_counts()
survival_counts.plot(kind='bar', color=['#8e7cc3', '#a2c4c9'])
plt.title("Sobrevivientes vs. Fallecidos")
plt.xlabel("Estado")
plt.ylabel("Cantidad de Pasajeros")
plt.xticks([0, 1], ['Fallecidos', 'Sobrevivientes'])
plt.show()

#Cantidad de mujeres y hombres que murieron:
gender_survival_counts = datos.groupby(['Sex', 'Survived']).size().unstack()
gender_survival_counts.plot(kind='bar', stacked=True, color=['#8e7cc3', '#a2c4c9'])
plt.title("Sobrevivientes y Fallecidos por Género")
plt.xlabel("Género")
plt.ylabel("Cantidad de Pasajeros")
plt.xticks(rotation=0)
plt.legend(['Fallecidos', 'Sobrevivientes'])
plt.show()

#Sobrevivientes por Clase
class_survival_counts = datos.groupby(['Pclass', 'Survived']).size().unstack()
class_survival_counts.plot(kind='bar', stacked=True, color=['#8e7cc3', '#a2c4c9'])
plt.title("Sobrevivientes por Clase")
plt.xlabel("Clase")
plt.ylabel("Cantidad de Pasajeros")
plt.xticks(rotation=0)
plt.legend(['Fallecidos', 'Sobrevivientes'], loc='upper right')
plt.show()


# Elimina las filas que contienen valores nulos
datos = datos.dropna(how='any')

# Edad media de los pasajeros:

# Calcular la edad media
edad_media = datos['Age'].mean()
#Distribución de Edades de los Pasajeros
plt.figure(figsize=(8, 6))
sns.boxplot(y='Age', data=datos, width=0.5)
plt.title(f'Edad Media: {edad_media:.2f}')
plt.ylabel("Edad")
plt.show()

# Filtra los datos para el rango de edades de 20 a 30 años y selecciona solo las personas fallecidas
fallecidos_entre_20_y_30 = titanic[(titanic['Age'] >= 20) & (titanic['Age'] < 31) & (titanic['Survived'] == 0)]

# Calcula las frecuencias y los bordes de los intervalos
frecuencias, bordes_intervalos, _ = plt.hist(fallecidos_entre_20_y_30['Age'], bins=10, color='#8e7cc3', edgecolor='black')

# Crea un histograma
plt.figure(figsize=(8, 6))
plt.hist(fallecidos_entre_20_y_30['Age'], bins=10, color='#8e7cc3', edgecolor='black')
plt.title("Cantidad de Personas Fallecidas entre 20 y 30 años")
plt.xlabel("Edad")
plt.ylabel("Cantidad de Fallecidos")

# Agrega las frecuencias en las barras del histograma
for i, freq in enumerate(frecuencias):
    plt.text(bordes_intervalos[i], freq, str(int(freq)), ha='center', va='bottom', fontsize=10, color='black')

plt.show()




