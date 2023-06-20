import matplotlib.pyplot as plt
import numpy as np
import random


def calcular(θ1, lista_datos):
    return sum([(θ1 * obj[0] - obj[1]) ** 2 for obj in lista_datos]) / (2 * len(lista_datos))


def calcular_error(θ1, lista_datos):
    return sum([abs((θ1 * obj[0] - obj[1])) for obj in lista_datos]) / len(lista_datos)


#lista_datos = [[1, 1], [2, 2], [3, 3]]
# Numeros Enteros
# lista_datos = [[random.randint(1, 100), random.randint(1, 50)] for i in range(1000)]
# Numeros Decimales
lista_datos = [[random.uniform(1, 100), random.uniform(1, 100)] for i in range(1000)]

lista_jDatos = []
lista_θDatos = []
lista_error = []

factor = 0.25
θ1 = -5
jValor = calcular(θ1, lista_datos)
lista_jDatos.append(jValor)
lista_θDatos.append(θ1)
lista_error.append(calcular_error(θ1, lista_datos))
print("θ1: ", θ1, ", Valor: ", round(jValor,5), ", Error: ", calcular_error(θ1, lista_datos))

mejorθ = θ1
while True:
    θ1 += factor
    jNuevo = calcular(θ1, lista_datos)
    if jValor > jNuevo:
        jValor = jNuevo
        mejorθ = θ1
        lista_jDatos.append(jNuevo)
        lista_θDatos.append(mejorθ)
        lista_error.append(calcular_error(mejorθ, lista_datos))
        print("θ1: ", θ1, ", Valor: ", round(jNuevo,5), ", Error: ", calcular_error(mejorθ, lista_datos))
    else:
        break

# Crear la figura y los subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# Gráfico de error
axs[0].plot(lista_θDatos, lista_error)
axs[0].set_title("Gráfico del error")
axs[0].set_xlabel("θ1")
axs[0].set_ylabel("Error")

# Gráfico de J(θ1)
axs[1].plot(lista_θDatos, lista_jDatos)
axs[1].set_title("Gráfico de la función J(θ1)")
axs[1].set_xlabel("θ1")
axs[1].set_ylabel("J(θ1)")

# Ajustar los subplots y mostrar la figura
fig.tight_layout()
plt.show()

# Crea un conjunto de puntos aleatorios
x = [punto[0] for punto in lista_datos]
y = [punto[1] for punto in lista_datos]

# Crea una función sinusoidal
x_func = np.linspace(min(x), max(x), 100)
y_func = mejorθ * x_func

# Grafica los puntos y la función
fig, ax = plt.subplots()
ax.scatter(x, y, label='Puntos')
ax.plot(x_func, y_func, label='Función', color='red')
ax.set_title("Gráfico de puntos y función h(x)=" + str(mejorθ) + "x")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()
