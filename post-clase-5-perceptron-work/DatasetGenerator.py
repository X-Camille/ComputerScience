import random
import math
import matplotlib.pyplot as plt

class DatasetGenerator:
    def __init__(self, num_examples=100):
        self.num_examples = num_examples

    def generate_linear_data(self):
        linear_data = []
        for _ in range(self.num_examples):
            slope = random.uniform(-5, 5)  # Pendiente aleatoria
            intercept = random.uniform(-5, 5)  # Intersección aleatoria
            points = [[j, slope * j + intercept] for j in range(10)]  # Movimiento lineal
            linear_data.append(points)
        return linear_data

    def generate_circular_data(self):
        circular_data = []
        for _ in range(self.num_examples):
            radius = random.uniform(3, 7)  # Variar el radio del círculo
            angle_offset = random.uniform(0, 2 * math.pi)  # Ángulo inicial aleatorio
            points = []
            for j in range(10):
                angle = angle_offset + (j / 10) * (2 * math.pi)  # Dividir el círculo en 10 pasos
                x = radius * math.cos(angle)      # Coordenada x
                y = radius * math.sin(angle)      # Coordenada y
                points.append([x, y])
            circular_data.append(points)
        return circular_data

    def generate_random_data(self):
        random_data = []
        for _ in range(self.num_examples):
            points = []
            for j in range(10):
                x = random.uniform(-10, 10)  # Generar valores x aleatorios
                y = random.uniform(-10, 10)  # Generar valores y aleatorios
                points.append([x, y])
            random_data.append(points)
        return random_data

    def generate_datasets(self):
        linear_data = self.generate_linear_data()
        circular_data = self.generate_circular_data()
        random_data = self.generate_random_data()

        return {
            "linear": linear_data,
            "circular": circular_data,
            "random": random_data
        }

# Uso del generador de conjuntos de datos
generator = DatasetGenerator()
datasets = generator.generate_datasets()

# Verificar los resultados
for key, value in datasets.items():
    print(f"{key.capitalize()} dataset example: {value[0]}")

# Crear gráficos
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Graficar datos lineales
linear_points = datasets["linear"][0]
x_linear, y_linear = zip(*linear_points)
axs[0].plot(x_linear, y_linear, marker='o')
axs[0].set_title('Movimiento Lineal')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')
axs[0].grid()

# Graficar datos circulares
circular_points = datasets["circular"][0]
x_circular, y_circular = zip(*circular_points)
axs[1].plot(x_circular, y_circular, marker='o')
axs[1].set_title('Movimiento Circular')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Y')
axs[1].grid()

# Graficar datos aleatorios
random_points = datasets["random"][0]
x_random, y_random = zip(*random_points)
axs[2].scatter(x_random, y_random)
axs[2].set_title('Movimiento Aleatorio')
axs[2].set_xlabel('X')
axs[2].set_ylabel('Y')
axs[2].grid()

# Mostrar gráficos
plt.tight_layout()
plt.show()
