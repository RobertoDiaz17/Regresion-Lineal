import numpy as np
import matplotlib.pyplot as plt

# Datos de la imagen
carga_kN = np.array([5, 10, 15, 20, 25])
elongacion_mm = np.array([0.6, 1.2, 1.9, 2.5, 3.1])

# Cálculo de los coeficientes de la regresión lineal
n = len(carga_kN)
sum_x = np.sum(carga_kN)
sum_y = np.sum(elongacion_mm)
sum_xy = np.sum(carga_kN * elongacion_mm)
sum_x2 = np.sum(carga_kN**2)

# Fórmulas de regresión lineal
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print(f"Coeficientes de la regresión:")
print(f"a (intercepto) = {a:.4f}")
print(f"b (pendiente) = {b:.4f}")

# Predicción usando el modelo
elongacion_pred_mm = a + b * carga_kN

# Gráfica
plt.figure(figsize=(8, 6))
plt.plot(carga_kN, elongacion_mm, 'o', label='Datos medidos')
plt.plot(carga_kN, elongacion_pred_mm, '-', label=f'Ajuste lineal: y = {a:.2f} + {b:.2f}x', color='red')
plt.xlabel('Carga (kN)')
plt.ylabel('Elongación (mm)')
plt.title('Relación entre Carga y Elongación en una Barra de Acero')
plt.legend()
plt.grid(True)
plt.savefig('resistencia_materiales.png', dpi=300)
plt.show()