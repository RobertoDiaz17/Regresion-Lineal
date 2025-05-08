import numpy as np
import matplotlib.pyplot as plt

# Datos de la imagen
presion_kPa = np.array([50, 70, 90, 110, 130])
caudal_Lmin = np.array([15, 21, 27, 33, 39])

# Cálculo de los coeficientes de la regresión lineal
n = len(presion_kPa)
sum_x = np.sum(presion_kPa)
sum_y = np.sum(caudal_Lmin)
sum_xy = np.sum(presion_kPa * caudal_Lmin)
sum_x2 = np.sum(presion_kPa**2)

# Fórmulas de regresión lineal
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print(f"Coeficientes de la regresión:")
print(f"a (intercepto) = {a:.4f}")
print(f"b (pendiente) = {b:.4f}")

# Predicción usando el modelo
caudal_pred_Lmin = a + b * presion_kPa

# Predicción del caudal cuando la presión es 100 kPa
presion_prediccion = 100
caudal_prediccion_Lmin = a + b * presion_prediccion
print(f"\nCaudal predicho para una presión de {presion_prediccion} kPa: {caudal_prediccion_Lmin:.2f} L/min")

# Gráfica
plt.figure(figsize=(8, 6))
plt.plot(presion_kPa, caudal_Lmin, 'o', label='Datos medidos')
plt.plot(presion_kPa, caudal_pred_Lmin, '-', label=f'Ajuste lineal: y = {a:.2f} + {b:.2f}x', color='red')
plt.scatter(presion_prediccion, caudal_prediccion_Lmin, color='green', marker='x', s=100, label=f'Predicción a {presion_prediccion} kPa')
plt.xlabel('Presión (kPa)')
plt.ylabel('Caudal (L/min)')
plt.title('Relación entre Presión y Caudal en una Tubería')
plt.legend()
plt.grid(True)
plt.savefig('caudal_tuberias.png', dpi=300)
plt.show()