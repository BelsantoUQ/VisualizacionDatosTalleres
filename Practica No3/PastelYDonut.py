import matplotlib.pyplot as plt

# Datos de ventas totales en millones
marcas = ['Kia', 'Toyota', 'Nissan', 'Honda', 'Audi']
ventas_millones = [10.5, 15.3, 14.2, 16.1, 9.8]

# Gráfico de Pastel
plt.figure(figsize=(8, 8))
plt.pie(ventas_millones, labels=marcas, autopct='%1.1f%%', startangle=140)
plt.title('Ventas de Autos en EE.UU. por Marca')

# Gráfico de Donut (Anillo)
plt.figure(figsize=(8, 8))
plt.pie(ventas_millones, labels=marcas, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.4, edgecolor='w'))
plt.title('Ventas de Autos en EE.UU. por Marca (Donut)')

# Mostrar ambos gráficos
plt.show()
