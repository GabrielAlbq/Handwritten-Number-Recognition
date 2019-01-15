import json
import math
from scipy.special import expit

class Cell:
    """
    Implementação da funcionalidade de uma célula da rede neural perceptron
    """

    def __init__(self, input_, number, expected_output):
        self.input_ = input_  # lista com os dados da imagem
        self.number = number  # número correto que representa a imagem
        self.expected_output = expected_output  # saída esperada (no caso, 1)
        self.learning_rate = 0.001 # taxa de aprendizado
        self.threshold = 0.5  # limiar

        # carregar os pesos armazenados no arquivos weights.json
        with open('weights.json') as file:
            self.previous_weights = json.load(file)
            self.weights = self.previous_weights[self.number]

        self.calc_sum()
        #print(self.output)
        # caso a saída seja errada (saída 0), os pesos são atualizados
        if self.output == 0:
            print("entrou")
            self.error = self.expected_output - self.output
            self.att_weights()

        self.save_weights()

    def calc_sum(self):
        """
        Multiplica todas as posições da lista de entrada por todas as posições
        da lista de peso (entrada[x] * pesos[x]), soma todos os valores
        e define a saída de acordo com a soma obtida
        """
        self.input_weights = []

        for i in range(784):
            #norm = self.input_[i] / 255
            #print(self.input_[i])
            #print(norm)
            #self.input_weights.append(norm * self.weights[i])
            self.input_weights.append(self.input_[i] * self.weights[i])

        #print(self.input_weights)
        self.output = sum(self.input_weights)
        #print(self.output)
        #self.output = sigmoid_derivative(self.output)
        #self.output = expit(self.output)
        #print(self.output)
        #aux = sigmoid(self.output)
        #self.output = aux
        self.output = sigmoid(self.output)
        #print(self.output)
        self.output = self.loss_func(self.output)
        #print(self.output)

    def att_weights(self):
        """
        Atualiza os pesos caso a saída for "errada" (saída 0)
        """
        for i in range(784):
            self.weights[i] = self.weights[i] + self.learning_rate * self.error * self.input_[i]

    def save_weights(self):
        """
        Salva os pesos no arquivo weights.json (a função deve ser chamada após
        ocorrer a atualização dos pesos)
        """
        self.previous_weights[self.number] = self.weights
        with open('weights.json', 'w') as file:
            json.dump(self.previous_weights, file)

    def loss_func(self, output):
        """
        Função perda, compara o resultado da soma (entradas * pesos) com
        o limiar e retorna a saída (0 ou 1) de acordo com o resultado
        """
        return 1 if output >= self.threshold else 0


def sigmoid(output):
    """
    Função sigmóide
    """
    x = (1/(1+math.exp(-output)))
    return 1 / (1 + math.exp(-output))
    #return x
    #return 1 / (1 + math.exp(-2 * output))


def sigmoid_derivative(output):
    """
    Função sigmóide derivada
    """
    x = sigmoid(output)
    #return 1 - (math.pow(x, 2))
    return 1 - x

def normalizar(array):
    aux = []
    for i in array:
        aux.append(i / 255)
    return aux