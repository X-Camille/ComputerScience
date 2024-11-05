import math
import random
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

def generate_dataset():
    linear_data = generate_linear_data()
    circular_data = generate_circular_data()
    random_data = generate_random_data()
    return [linear_data, circular_data, random_data]

def graficar_dataset(dataset):
    # Crear gráficos
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    # Graficar datos lineales
    linear_points = dataset[0]
    x_linear, y_linear = zip(*linear_points)
    axs[0].plot(x_linear, y_linear, marker='o')
    axs[0].set_title('Movimiento Lineal')
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('Y')
    axs[0].grid()

    # Graficar datos circulares
    circular_points = dataset[1]
    x_circular, y_circular = zip(*circular_points)
    axs[1].plot(x_circular, y_circular, marker='o')
    axs[1].set_title('Movimiento Circular')
    axs[1].set_xlabel('X')
    axs[1].set_ylabel('Y')
    axs[1].grid()

    # Graficar datos aleatorios
    random_points = dataset[2]
    x_random, y_random = zip(*random_points)
    axs[2].scatter(x_random, y_random)
    axs[2].set_title('Movimiento Aleatorio')
    axs[2].set_xlabel('X')
    axs[2].set_ylabel('Y')
    axs[2].grid()

    # Mostrar gráficos
    plt.tight_layout()
    plt.show()

class Perceptron:
    def __init__(self):
        self.input_size = 10  
        self.hidden_size = 5
        self.output_size = 3
        
        # Inicialización de los pesos con valores aleatorios pequeños
        self.w_input_hidden = [[random.uniform(-0.02, 0.02) for _ in range(self.input_size)] for _ in range(self.hidden_size)]
        self.w_hidden_output = [[random.uniform(-0.02, 0.02) + i*0.5 for i in range(self.hidden_size)] for _ in range(self.output_size)]
        
        # Sesgos
        self.bias_hidden = [0.5 + i for i in range(self.hidden_size)]
        self.bias_output = [-2 + j for j in range(self.output_size)]
        
        # Tasa de aprendizaje
        self.learning_rate = 0.01
        
    def set_learning_rate(self, learning_rate):
        self.learning_rate = learning_rate;
    
    def sigmoid(self, x):
        # Limita x al rango de -709 a 709
        if x < -709:
            x = -709
            x = -709
        elif x > 709:
            x = 709
        return 1 / (1 + math.exp(-x))

    def softmax(self, x):
        max_val = max(x) 
        exp_x = [math.exp(i - max_val) for i in x]  
        sum_exp_x = sum(exp_x)  
        return [i / sum_exp_x for i in exp_x] 

    def forward(self, dataset):
        hidden_input = [0] * self.hidden_size

        # Calcular la entrada de la capa oculta
        for j in range(self.hidden_size):
            for i in range(self.input_size):
                hidden_input[j] += self.w_input_hidden[j][i] * dataset[i][0] + self.w_input_hidden[j][i] * dataset[i][1]
            hidden_input[j] += self.bias_hidden[j]  

        # Aplicar función de activación 
        hidden_output = [self.sigmoid(val) for val in hidden_input]
        
        # Calcular entrada de la capa de salida
        output_input = [0] * self.output_size
        
        for k in range(self.output_size):
            for j in range(self.hidden_size):
                output_input[k] += hidden_output[j] * self.w_hidden_output[k][j]
            output_input[k] += self.bias_output[k]
        
        # Aplicar softmax para obtener la salida
        output = self.softmax(output_input)
        
        return output, hidden_output 

    def backpropagate(self, dataset, expected_set):
        output, hidden_output = self.forward(dataset)
                
        output_error = [expected_set[i] - output[i] for i in range(self.output_size)]
        
        # Gradiente de la capa de salida
        output_delta = [output_error[i] * output[i] * (1 - output[i]) 
                        for i in range(self.output_size)]

        # Actualizar pesos de la capa oculta a la capa de salida
        for k in range(self.output_size):
            for j in range(self.hidden_size):
                self.w_hidden_output[k][j] += self.learning_rate * output_delta[k] * hidden_output[j]
            self.bias_output[k] += self.learning_rate * output_delta[k]
        
        # Calcular el error en la capa oculta
        hidden_error = [0] * self.hidden_size
        for k in range(self.output_size):
            for j in range(self.hidden_size):
                hidden_error[j] += output_delta[k] * self.w_hidden_output[k][j]
        
        # Gradiente de la capa oculta
        hidden_delta = [hidden_error[j] * hidden_output[j] * (1 - hidden_output[j]) for j in range(self.hidden_size)]

        # Actualizar pesos de la capa de entrada a la capa oculta
        for j in range(self.hidden_size):
            for i in range(self.input_size):
                self.w_input_hidden[j][i] += self.learning_rate * hidden_delta[j] * dataset[i][0]
                self.w_input_hidden[j][i] += self.learning_rate * hidden_delta[j] * dataset[i][1]
            self.bias_hidden[j] += self.learning_rate * hidden_delta[j]
        
        return output  # Retornar el output para calcular MSE

perceptron = Perceptron()

def get_perceptron_output(output):
    if output[0] > output[1] and output[0] > output[2]:
        return "Linea"
    elif output[1] > output[0] and output[1] > output[2]:
        return "Circulo"
    else:
        return "Random"
    
def generate_datasets(num_sets):
    datasets = []
    for _ in range(num_sets):
        dataset = generate_dataset()  # Cada dataset con datos de cada clase
        datasets.append(dataset)
    return datasets

# Función para entrenar y calcular MSE
def training_set(epochs, num_sets):
    mse_values = []  # Almacena los valores de MSE por época
    datasets = generate_datasets(num_sets)
    for epoch in range(epochs):
        total_mse = 0  
        for dataset in datasets: 
            expected_set = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]   
            for i in range(len(dataset)):  
                output = perceptron.backpropagate(dataset[i], expected_set[i])
                
                # Calcular MSE para esta instancia
                total_mse += sum((expected_set[i][j] - output[j]) ** 2 for j in range(len(expected_set[i]))) / len(expected_set[i])
        
        # Calcular el MSE promedio para esta época
        mse = total_mse / num_sets
        mse_values.append(mse)  # Agregar MSE a la lista
        
        print(f"Época {epoch + 1}, MSE: {mse:.4f}")  # Imprimir MSE de la época

    # Graficar MSE
    plt.plot(range(1, epochs + 1), mse_values, marker='o')
    plt.title('Error Cuadrático Medio durante el Entrenamiento')
    plt.xlabel('Época')
    plt.ylabel('MSE')
    plt.grid()
    plt.show()
    print(f"Entrenamiento completado: {num_sets} imágenes en {epochs} épocas.")


# Evaluar el perceptrón
def evaluate_perceptron():
    overall_accuracy = 0
    num_sets = 30
    total = 0
    correct = 0
    correct_counts = {"Linea": 0, "Circulo": 0, "Random": 0}  # Conteo por clase
    expected_datasets = ["Linea", "Circulo", "Random"]

    print(f"Procesando conjunto de prueba de {num_sets} imágenes...")
    for n in range(num_sets):
        dataset = generate_dataset()
        print(f"---------------DATASET {n}---------------")
        for i in range(len(dataset)):
            output, _ = perceptron.forward(dataset[i])
            answer = get_perceptron_output(output)
            type_set = ""
            if i == 0:
                type_set = "Linea"
            elif i == 1:
                type_set = "Circulo"
            else: 
                type_set = "Random"
            if answer == expected_datasets[i]:
                print(f"Real: {type_set} -> Predicción: {answer}: Correcto")
                correct += 1
                correct_counts[answer] += 1
            else:
                print(f"Real: {type_set} -> Predicción: {answer}: INCORRECTO")
            total += 1

    # Calcular y mostrar porcentajes
    print("\nEvaluación del Perceptrón:")
    for key in correct_counts:
        if total > 0:  # Evita la división por cero
            percentage = (correct_counts[key] / 30) * 100
            print(f"Porcentaje de aciertos para {key}: {percentage:.2f}%")
        else:
            print(f"No se realizaron evaluaciones para {key}.")

    overall_accuracy = (correct / total) * 100 if total > 0 else 0
    
    print(f"\nPrecisión total: {overall_accuracy:.2f}%")
    
    return overall_accuracy

def evaluate_multiple_times(num):
    total_success_rates = []

    for _ in range(num):
        overall_accuracy = evaluate_perceptron()  
        total_success_rates.append(overall_accuracy)

    # Calcular el promedio de las tasas de éxito
    average_success_rate = sum(total_success_rates) / len(total_success_rates)
    
    print("")
    print("----------Evaluando múltiples veces----------")
    for i in range(len(total_success_rates)):
        print(f"\nPrecisión total: {total_success_rates[i]:.2f}%")

    print(f"\nPrecisión total promedio: {average_success_rate:.2f}%")
    
    return average_success_rate

def menu():
    while True:
        print("------------Menú------------")
        print("1. Entrenar perceptrón con 100 conjuntos de datos por cada categoría (Instrucción Preclase)")
        print("2. Entrenar perceptrón con 1000 conjuntos de datos por cada categoría (Adicional)")
        print("3. Visualizar gráfica de conjunto de datos aleatorio")
        print("0. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            perceptron.set_learning_rate(0.009)
            training_set(500, 100)
            evaluate_perceptron() # Evalúa el perceptrón una vez
            evaluate_multiple_times(10) # Evalúa el perceptrón múltiples veces
        elif opcion == "2":
            perceptron.set_learning_rate(0.001)
            training_set(200, 1000)
            evaluate_perceptron() 
            evaluate_multiple_times(10) 
        elif opcion == "3":
            dataset = generate_dataset()
            graficar_dataset(dataset)
        elif opcion == "0":
            break;
        else: 
            print("Opción no válida. Inténtenlo de nuevo.")
            
menu()