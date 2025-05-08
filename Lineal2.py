import numpy as np
import matplotlib.pyplot as plt

# Datos de la imagen
posicion_cm = np.array([0, 2, 4, 6, 8])
temperatura_C = np.array([100, 92, 85, 78, 71])

# Cálculo de los coeficientes de la regresión lineal
n = len(posicion_cm)
sum_x = np.sum(posicion_cm)
sum_y = np.sum(temperatura_C)
sum_xy = np.sum(posicion_cm * temperatura_C)
sum_x2 = np.sum(posicion_cm**2)

# Fórmulas de regresión lineal
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print(f"Coeficientes de la regresión:")
print(f"a (intercepto) = {a:.4f}")
print(f"b (pendiente) = {b:.4f}")

# Predicción usando el modelo
temperatura_pred_C = a + b * posicion_cm

# Estimar la temperatura en x = 5 cm
posicion_estimada = 5
temperatura_estimada_C = a + b * posicion_estimada
print(f"\nTemperatura estimada en x = {posicion_estimada} cm: {temperatura_estimada_C:.2f} °C")

# Gráfica
plt.figure(figsize=(8, 6))
plt.plot(posicion_cm, temperatura_C, 'o', label='Datos medidos')
plt.plot(posicion_cm, temperatura_pred_C, '-', label=f'Ajuste lineal: y = {a:.2f} + {b:.2f}x', color='red')
plt.scatter(posicion_estimada, temperatura_estimada_C, color='green', marker='x', s=100, label=f'Estimación en x = {posicion_estimada} cm')
plt.xlabel('Posición (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Disminución de la Temperatura a lo Largo de una Barra')
plt.legend()
plt.grid(True)
plt.savefig('transferencia_calor.png', dpi=300)
plt.show()