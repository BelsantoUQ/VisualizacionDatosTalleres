import pandas as pd
import matplotlib.pyplot as plt

# Cargar el conjunto de datos y seleccionar las columnas relevantes
df = pd.read_csv("C:/Users/USER/Documents/Programacion/python/VisualizacionDatos/VisualizacionDatosTalleres/PEC 1/appstore_games.csv")
df = df[['Average User Rating', 'Size', 'Price', 'Description', 'Age Rating']]

# Eliminar filas con valores nulos en las columnas relevantes
df.dropna(subset=['Average User Rating', 'Size', 'Price', 'Description', 'Age Rating'], inplace=True)

# Crear histograma del Age Rating en el rango de Average User Rating mayor a 3
size_filter = df['Average User Rating'] > 4
plt.figure(figsize=(10, 6))
plt.hist(df[size_filter]['Age Rating'], bins=10,color='#a2c4c9', edgecolor='k')
plt.xlabel('Age Rating')
plt.ylabel('Frecuencia')
plt.title('Histograma del rating de edad (Puntuación mayor a 4)')
plt.show()

# Filtrar los datos cuyo precio es menor a 5 dólares
df_filtered = df[df['Price'] < 5]

# Crear un histograma del tamaño (Size) para juegos con precio < $5
plt.figure(figsize=(10, 6))
frecuencias, bins, _ = plt.hist(df_filtered['Size'], bins=20, color='#8e7cc3', edgecolor='k', alpha=0.7)
plt.title('Distribución del Tamaño de Juegos (para juegos con precio < $5)')
plt.xlabel('Tamaño (MB)')
plt.ylabel('Frecuencia')
plt.grid(True)

# Imprimir las frecuencias
for i, frecuencia in enumerate(frecuencias):
    plt.text(bins[i], frecuencia, str(int(frecuencia)), ha='center', va='bottom')

plt.show()


# Filtrar juegos que contienen la palabra clave "Sudoku" en la descripción
endless_runner_filter = df['Description'].str.contains('endless runner', case=False)

# Crear un histograma del Average User Rating para estos juegos
plt.figure(figsize=(10, 6))
frecuencia_mas_alta = plt.hist(df[endless_runner_filter]['Average User Rating'], bins=10, color='#a2c4c9', edgecolor='k')[0].max()
plt.xlabel('Average User Rating')
plt.ylabel('Frecuencia')
plt.title('Calificación de Juegos "Endless Runner"')

# Calcular la frecuencia más alta

# Marcar la frecuencia más alta en el eje y con una línea horizontal
plt.axhline(frecuencia_mas_alta, color='#134f5c', linestyle='--', label=f'Frecuencia Más Alta {frecuencia_mas_alta}')
plt.legend()
plt.show()

# Filtrar juegos que contienen la palabra clave "Sudoku" en la descripción
endless_runner_filter = df['Description'].str.contains('Sudoku', case=False)

# Crear un histograma del Average User Rating para estos juegos
plt.figure(figsize=(10, 6))
frecuencia_mas_alta = plt.hist(df[endless_runner_filter]['Average User Rating'], bins=10, color='#8e7cc3', edgecolor='k')[0].max()
plt.xlabel('Average User Rating')
plt.ylabel('Frecuencia')
plt.title('Calificación de Juegos "Sudoku"')

# Calcular la frecuencia más alta

# Marcar la frecuencia más alta en el eje y con una línea horizontal
plt.axhline(frecuencia_mas_alta, color='#134f5c', linestyle='--', label=f'Frecuencia Más Alta {frecuencia_mas_alta}')
plt.legend()
plt.show()


