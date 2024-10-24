import math
import random

# Generadores de imágenes
def generate_line_image():
    row_selector = random.randint(0, 9)
    orientation = 0
    line_image = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if orientation == 0 and i == row_selector:
                line_image[i][j] = 1
            elif orientation == 1 and j == row_selector:
                line_image[i][j] = 1
    return line_image

def generate_circle_image():
    radius = random.randint(1, 4)  # Limitado a un máximo de 4 para que el círculo quepa en la imagen 10x10
    center_x = random.randint(radius, 9 - radius)  # Asegura que el círculo no se salga de los bordes
    center_y = random.randint(radius, 9 - radius)
    
    circle_image = [[0 for _ in range(10)] for _ in range(10)] 
    
    # Llenar la imagen con el círculo
    for i in range(10):
        for j in range(10):
            if (i - center_x) ** 2 + (j - center_y) ** 2 <= radius ** 2:
                circle_image[i][j] = 1  
    
    return circle_image

def showPicture(x_input):
    for i in range(10):
        for j in range(10):
            print(x_input[i][j], end=" ")
        print()

# Funciones de Activación
def softmax(z):
    exp_values = [math.exp(i) for i in z]
    sum_exp = sum(exp_values)
    return [j / sum_exp for j in exp_values]

def step(z, threshold=0):
    return 1 if z > threshold else 0

# Red Neuronal
def generate_weights(input_size, hidden_size, output_size=2):
    w_input_weights = [[-1+0.1*k if i <= 27 or i >= 36 else -1 for i in range(input_size)] for k in range(hidden_size)]
    w_hidden_weights = [[0.4 if k == 0 else -5+i for i in range(hidden_size)] for k in range(output_size)]
    return w_input_weights, w_hidden_weights

def perceptron(x_input):
    input_size = 100  # 10x10 imagen
    hidden_size = 10
    output_size = 2  # 2 opciones: línea o círculo
    
    hidden_layer_output = []  # Para almacenar la salida de la capa oculta
    hidden_bias = 10
    output_bias = 10
    
    w_input_weights, w_hidden_weights = generate_weights(input_size, hidden_size)
  
    # Capa oculta
    for i in range(hidden_size):
        weighted_sum = 0
        for j in range(input_size):
            index = j // 10  # Filas
            column = j % 10  # Columnas
            weighted_sum += x_input[index][column] * w_input_weights[i][j]
        weighted_sum += hidden_bias
        hidden_layer_output.append(step(weighted_sum))  # Aplicar la función escalón
    print(hidden_layer_output)
    
    # Calcular la suma ponderada para cada clase en la capa de salida
    weighted_sums = [0] * output_size  # Inicializa las sumas para cada clase

    for k in range(output_size):
        for i in range(hidden_size):
            weighted_sums[k] += hidden_layer_output[i] * w_hidden_weights[k][i]  # Usar pesos específicos para cada clase
        weighted_sums[k] += output_bias
    print(weighted_sums)

    # Aplicar softmax para obtener probabilidades
    probabilities = softmax(weighted_sums)
    return probabilities

def create_image_test():
    labels = []
    x_inputs = []
    for i in range(2):
        if i % 2 == 0:
            x_inputs.append(generate_line_image())
            labels.append(1)  # Clase 1: Línea
        else:
            x_inputs.append(generate_circle_image())
            labels.append(2)  # Clase 2: Círculo
    return labels, x_inputs

def main():
    hidden_size = 10  # Tamaño de la capa oculta
    output_size = 2   # Número de clases (línea y círculo)

    labels, x_inputs = create_image_test()
    
    total_tests = len(x_inputs)
    correct_predictions = 0
        
    for i in range(total_tests):
        output_probabilities = perceptron(x_inputs[i])
        if output_probabilities[0] > output_probabilities[1] and labels[i] == 1:
            correct_predictions += 1
        elif output_probabilities[0] < output_probabilities[1] and labels[i] == 2:
            correct_predictions += 1

    accuracy = (correct_predictions / total_tests) * 100
    return accuracy  # Cambiar print por return para acumular el accuracy

# Inicializar variables para calcular el promedio
total_accuracy = 0
num_executions = 30

for i in range(num_executions):
    total_accuracy += main()  # Acumula el accuracy de cada ejecución

# Calcular y mostrar el promedio
average_accuracy = total_accuracy / num_executions
print(f"El promedio de éxito en las pruebas ha sido del: {average_accuracy}%")