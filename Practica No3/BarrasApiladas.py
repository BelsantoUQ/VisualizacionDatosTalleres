import matplotlib.pyplot as plt
# Este tipo de gráfico es útil para mostrar la distribución de las ventas de 
# diferentes marcas de autos a lo largo de varios días en Europa. Aquí, se utiliza 
# un gráfico de barras apiladas para representar las ventas diarias de Toyota, Nissan y Audi.
# En este gráfico, las barras apiladas muestran las ventas diarias de Toyota, Audi 
# y Nissan  durante cinco días en Europa. Es útil para comparar 
# la contribución de cada marca en las ventas totales por día.

# Datos de ventas diarias
dias = ['Día 1', 'Día 2', 'Día 3', 'Día 4', 'Día 5']
ventas_toyota = [10, 15, 19, 9, 0]
ventas_audi = [15, 25, 27, 24, 28]
ventas_nissan = [9, 30, 15, 20, 17]

# Crear el gráfico de barras apiladas
plt.figure(figsize=(10, 6))
plt.bar(dias, ventas_toyota, label='Toyota', color='yellow')
plt.bar(dias, ventas_audi, label='Audi', bottom=ventas_toyota, color='orange')
plt.bar(dias, ventas_audi, label='Nissan', bottom=ventas_toyota, color='blue')

# Configuración de etiquetas y título
plt.xlabel('Días')
plt.ylabel('Ventas')
plt.title('Ventas de Autos en Europa por Marca y Día')
plt.legend()

# Mostrar el gráfico
plt.show()
