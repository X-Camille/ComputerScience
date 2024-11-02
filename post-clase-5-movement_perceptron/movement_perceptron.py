import math
import random
import datasets_generator
import matplotlib.pyplot as plt

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
        self.learning_rate = 0.01
    
    def sigmoid(self, x):
        # Limita x al rango de -709 a 709
        if x < -709:
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
        
        return output  # Retornar el output para calcular MSE

perceptron = Perceptron()

def get_perceptron_output(output):
    if output[0] > output[1] and output[0] > output[2]:
        return "Linea"
    elif output[1] > output[0] and output[1] > output[2]:
        return "Circulo"
    else:
        return "Random"

# Función para entrenar y calcular MSE
def training_set(epochs, num_sets):
    mse_values = []  # Almacena los valores de MSE por época
    for epoch in range(epochs):
        total_mse = 0  
        for _ in range(num_sets):   
            datasets = datasets_generator.generate_datasets()  # Cada dataset con datos de cada clase
            expected_set = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            for i in range(len(datasets)):  
                output = perceptron.backpropagate(datasets[i], expected_set[i])
                # Calcular MSE para este dataset
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
    
    training_set(350, 100)

    print(f"Procesando conjunto de prueba de {num_sets} imágenes...")
    for n in range(num_sets):
        datasets = datasets_generator.generate_datasets()
        print(f"---------------DATASET {n}---------------")
        for i in range(len(datasets)):
            output, _ = perceptron.forward(datasets[i])
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
    training_set(350, 100)  # Entrenar el perceptrón
    
    total_success_rates = []

    for _ in range(num):
        overall_accuracy = evaluate_perceptron()  
        total_success_rates.append(overall_accuracy)

    # Calcular el promedio de las tasas de éxito
    average_success_rate = sum(total_success_rates) / len(total_success_rates)
    
    for i in range(len(total_success_rates)):
        print(f"\nPrecisión total: {total_success_rates[i]:.2f}%")

    print(f"\nPrecisión total promedio: {average_success_rate:.2f}%")
    
    return average_success_rate


evaluate_perceptron() # Evalúa el perceptrón una vez
# evaluate_multiple_times(10) # Evalúa el perceptrón múltiples veces

            
        
