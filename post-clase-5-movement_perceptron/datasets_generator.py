import random
import math
import matplotlib.pyplot as plt

def generate_linear_data():
    linear_data = []
    slope = random.uniform(-10, 10)  # Pendiente aleatoria
    intercept = random.uniform(-5, 5)  # Intersección aleatoria
    points = [[j, slope * j + intercept] for j in range(10)]
    linear_data.extend(points)
    return linear_data

def generate_circular_data():
    circular_data = []
    radius = random.uniform(1, 7)  # Radio aleatorio
    angle_offset = random.uniform(0, 2 * math.pi)  # Ángulo inicial aleatorio
    points = []
    for j in range(10):
        angle = angle_offset + (j / 10) * (2 * math.pi) 
        x = radius * math.cos(angle)      # Coordenada x
        y = radius * math.sin(angle)      # Coordenada y
        points.append([x, y])
    circular_data.extend(points)
    return circular_data

def generate_random_data():
    random_data = []
    points = []
    for j in range(10):
        x = random.uniform(-10, 10)  # Valores x aleatorios
        y = random.uniform(-10, 10)  # Valores y aleatorios
        points.append([x, y])
    random_data.extend(points)
    return random_data

def generate_datasets():
    linear_data = generate_linear_data()
    circular_data = generate_circular_data()
    random_data = generate_random_data()
    return [linear_data, circular_data, random_data]

datasets = generate_datasets()

def graficar_dataset():
    # Crear gráficos
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    # Graficar datos lineales
    linear_points = datasets[0]
    x_linear, y_linear = zip(*linear_points)
    axs[0].plot(x_linear, y_linear, marker='o')
    axs[0].set_title('Movimiento Lineal')
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('Y')
    axs[0].grid()

    # Graficar datos circulares
    circular_points = datasets[1]
    x_circular, y_circular = zip(*circular_points)
    axs[1].plot(x_circular, y_circular, marker='o')
    axs[1].set_title('Movimiento Circular')
    axs[1].set_xlabel('X')
    axs[1].set_ylabel('Y')
    axs[1].grid()

    # Graficar datos aleatorios
    random_points = datasets[2]
    x_random, y_random = zip(*random_points)
    axs[2].scatter(x_random, y_random)
    axs[2].set_title('Movimiento Aleatorio')
    axs[2].set_xlabel('X')
    axs[2].set_ylabel('Y')
    axs[2].grid()

    # Mostrar gráficos
    plt.tight_layout()
    plt.show()

graficar_dataset()