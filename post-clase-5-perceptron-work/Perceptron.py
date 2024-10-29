import random
import math

class Perceptron:
    def __init__(self):
        self.input_size = 10  
        self.hidden_size = 5
        self.output_size = 3
        
        # Inicialización de los pesos
        self.w_input_hidden = [[-1 + 0.1 * k if i <= 27 or i >= 36 else -1 for i in range(self.input_size)] for k in range(self.hidden_size)]
        
        # Pesos entre la capa oculta y la capa de salida
        self.w_hidden_output = [[0.4 if k == 0 else -5 + i for i in range(self.hidden_size)] for k in range(self.output_size)]
        
        # Sesgos (biases)
        self.bias_hidden = 1
        self.bias_output = 2
    
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def softmax(self, x):
        exp_x = [math.exp(i) for i in x]  
        sum_exp_x = sum(exp_x)
        return [j / sum_exp_x for j in exp_x] 

    def forward(self, x):
        hidden_input = [0] * self.hidden_size
        
        # Calcular la entrada de la capa oculta
        for i in range(self.input_size):
            for j in range(self.hidden_size):
                hidden_input[j] += self.w_input_hidden[j][i] * x[i][0] + self.w_input_hidden[j][i] * x[i][1]
        
        # Agregar sesgo a la capa oculta
        for j in range(self.hidden_size):
            hidden_input[j] += self.bias_hidden  

        # Aplicar función de activación sigmoide
        hidden_output = [self.sigmoid(val) for val in hidden_input]
        
        # Calcular entrada de la capa de salida
        output_input = [0] * self.output_size
        for k in range(self.output_size):
            for j in range(self.hidden_size):
                output_input[k] += hidden_output[j] * self.w_hidden_output[k][j]
            output_input[k] += self.bias_output  # Agregar sesgo a la capa de salida
        
        # Aplicar softmax para obtener la salida
        output = self.softmax(output_input)
        return output

perceptron = Perceptron()

example_input = [[random.uniform(0, 1), random.uniform(0, 1)] for _ in range(10)]
output = perceptron.forward(example_input)
print(output)
