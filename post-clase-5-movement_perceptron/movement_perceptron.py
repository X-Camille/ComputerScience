import math
import random
import matplotlib.pyplot as plt

# Funciones de generación de datos se mantienen igual
def generate_linear_data():
    linear_data = []
    slope = random.uniform(-10, 10)  # Pendiente aleatoria
    intercept = random.uniform(-5, 5)  # Intersección aleatoria
    points = [[j, slope * j + intercept] for j in range(10)]  # Movimiento lineal
    linear_data.append(points)
    return linear_data

def generate_circular_data():
    circular_data = []
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

def generate_random_data():
    random_data = []
    points = []
    for j in range(10):
        x = random.uniform(-10, 10)  # Generar valores x aleatorios
        y = random.uniform(-10, 10)  # Generar valores y aleatorios
        points.append([x, y])
    random_data.append(points)
    return random_data

def generate_datasets():
    linear_data = generate_linear_data()
    circular_data = generate_circular_data()
    random_data = generate_random_data()
    return [linear_data, circular_data, random_data]
    
# Clase Perceptron se mantiene igual
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
        self.learning_rate = 0.1

    def get_bias_hidden(self):
        return self.bias_hidden
    
    def get_bias_output(self):
        return self.bias_output
    
    def get_w_input_hidden(self):
        return self.w_input_hidden
    
    def get_w_hidden_output(self):
        return self.w_hidden_output
    
    def sigmoid(self, x):
        # Limita x al rango de -709 a 709
        if x < -709:
            x = -709
        elif x > 709:
            x = 709
        return 1 / (1 + math.exp(-x))

    def softmax(self, x):
        max_val = max(x)  # Encuentra el valor máximo
        exp_x = [math.exp(i - max_val) for i in x]  # Resta el máximo
        sum_exp_x = sum(exp_x)  # Suma de las exponenciales
        return [i / sum_exp_x for i in exp_x]  # Normaliza

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
        output_delta = [output_error[i] * output[i] * (1 - output[i]) for i in range(self.output_size)]

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

perceptron = Perceptron()

def training_set(epochs, images):
    for _ in range(epochs):
        for _ in range(images):   
            datasets = generate_datasets()  # Cada dataset con datos de cada clase
            expected_set = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            for i in range(len(datasets)):  # Esto asegura que no salgas del rango
                perceptron.backpropagate(datasets[i][0], expected_set[i])
    print(f"Entrenamiento completado: {images} imágenes en {epochs} épocas")

def answer_perceptron(output):
    if output[0] > output[1] and output[0] > output[2]:
        return "Linea"
    elif output[1] > output[0] and output[1] > output[2]:
        return "Circulo"
    else:
        return "Random"
       
def evaluate_perceptron():
    overall_accuracy = 0
    images = 30
    total = 0
    correct = 0
    correct_counts = {"Linea": 0, "Circulo": 0, "Random": 0}  # Conteo por clase
    expected_datasets = ["Linea", "Circulo", "Random"]
    
    training_set(350, 100)  # Entrenar el perceptrón

    print(f"Procesando conjunto de prueba de {images} imágenes...")
    for _ in range(images):
        datasets = generate_datasets()
        for i in range(len(datasets)):
            output, _ = perceptron.forward(datasets[i][0])
            answer = answer_perceptron(output)

            if answer == expected_datasets[i]:
                correct += 1
                correct_counts[answer] += 1
            
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
    #print(f"Bias hidden: {perceptron.get_bias_hidden()}")
    #print(f"Bias output: {perceptron.get_bias_output()}")
    #print(f"W input hidden: {perceptron.get_w_input_hidden()}")
    #print(f"W output hidden: {perceptron.get_w_hidden_output()}")

evaluate_perceptron()


            
        
