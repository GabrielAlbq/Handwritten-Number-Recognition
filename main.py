from image_to_array import ImageToArray
from cell import Cell
import json
import random
import os
import os.path
import numpy as np

def load_images():
    """
    As imagens precisam estar divididas em pastas (uma para cada número)
    e devem possuir o nome do respectivo número.
    Exemplo:
    Pasta com imagens do número 1 = one
    Pasta com imagens do número 2 = two
    ...
    As pastas precisam estar no mesmo diretório em que o script é executado

    A função load_images percorre as pastas e as imagens e envia
    as imagens para a classe ImageToArray que retorna a imagem em forma de
    lista com o método get_array

    A função retorna um dicionário em que as chaves são os números e valor é
    uma lista em que cada posição é uma imagem convertida para array unidimensional
    """
    images = {'number0': [],
              'number1': [],
              'number2': [],
              'number3': [],
              'number4': [],
              'number5': [],
              'number6': [],
              'number7': [],
              'number8': [],
              'number9': []}

    for item in os.listdir():
        if item in list(images.keys()):
            if os.path.isdir(item):
                for file in os.listdir(item):
                    array = ImageToArray(f'{item}\\' + file)
                    images[item].append(array.get_array())
    return images

'''
def create_weights():
    """
    Caso o arquivo que armazena os pesos das entradas não exista,
    ele é criado e inicializado com valores aleatórios entre 0 e 1 (784 valores)

    O arquivo .json resultante possui o nome dos números como chaves e o valor
    é uma lista com 784 posições, cada uma dela corresponde a um valor
    """
    if not os.path.isfile('weights.json'):
        data = {"number0": [],
                "number1": [],
                "number2": [],
                "number3": [],
                "number4": [],
                "number5": [],
                "number6": [],
                "number7": [],
                "number8": [],
                "number9": []}

        for i in list(data.keys()):
            for j in range(784):
                data[i].append(round(random.uniform(-1, 0.05),3))  # pesos aleatórios entre 0 e 1

        with open('weights.json', 'w') as file:
            json.dump(data, file)


def learn(images):
    """
    O parâmetro images deve ser o dicinário que é obtido na função load_images

    A função percorre todas as chaves e valores do dicionário (consequentemente
    todas as imagens armazenadas anteriormente) e passa esses valores para a classe
    Cell que possui a implementação de uma rede neural perceptron e atualiza os pesos
    no arquivo de pesos .json
    """
    for a in range(10):
        for i in list(images.keys()):
            for j in range(len(images[i])):
                cell_ = Cell(images[i][j], i, 1)

'''
def check_result(image):
    """
    Recebe uma imagem como parametro, multiplica o seu vetor da imagem pelo
    vetor de imagem "aprendido" (que está no arquivo weights.json) e calcula
    o somatório, retorna uma string com o nome do número que tiver o maior
    somatório
    Exemplo de retorno:
    'one', 'two', 'three', ...
    """
    with open('weights.json') as file:
        data = json.loads(file.read())

    weights_results = {"number0": [],
                       "number1": [],
                       "number2": [],
                       "number3": [],
                       "number4": [],
                       "number5": [],
                       "number6": [],
                       "number7": [],
                       "number8": [],
                       "number9": []}

    max_sum = 0
    number_result = ''

    for i in list(data.keys()):
        for j in range(784):
            weights_results[i].append(image[j] * data[i][j])
        weights_results[i] = sum(weights_results[i])
        if weights_results[i] > max_sum:
            max_sum = weights_results[i]
            number_result = i

    return number_result


def check_accuracy(images):
    """
    O parâmetro images deve ser o dicinário que é obtido na função load_images

    A função percorre todas as chaves e valores do dicionário (consequentemente
    todas as imagens armazenadas anteriormente) e passa as imagens para a função
    check_result que verifica que número o algoritmo "acha" que é o correto de acordo
    com a imagem que foi passada como parâmetro

    A função possui o simples objetivo de organizar os dados para serem "printados"
    e assim facilitar uma análise da precisão de acertos do algoritmo
    """

    zero_images = 0
    correct_zero_output = 0
    for i in images['number0']:
        number = check_result(i)
        #print(number)
        if number == 'number0':
            correct_zero_output += 1
        zero_images += 1

    one_images = 0
    correct_one_output = 0
    for i in images['number1']:
        number = check_result(i)
        #print(number)
        if number == 'number1':
            correct_one_output += 1
        one_images += 1

    two_images = 0
    correct_two_output = 0
    for i in images['number2']:
        number = check_result(i)
        #print(number)
        if number == 'number2':
            correct_two_output += 1
        two_images += 1

    three_images = 0
    correct_three_output = 0
    for i in images['number3']:
        number = check_result(i)
        #print(number)
        if number == 'number3':
            correct_three_output += 1
        three_images += 1

    four_images = 0
    correct_four_output = 0
    for i in images['number4']:
        number = check_result(i)
        #print(number)
        if number == 'number4':
            correct_four_output += 1
        four_images += 1

    five_images = 0
    correct_five_output = 0
    for i in images['number5']:
        number = check_result(i)
        #print(number)
        if number == 'number5':
            correct_five_output += 1
        five_images += 1

    six_images = 0
    correct_six_output = 0
    for i in images['number6']:
        number = check_result(i)
        #print(number)
        if number == 'number6':
            correct_six_output += 1
        six_images += 1

    seven_images = 0
    correct_seven_output = 0
    for i in images['number7']:
        number = check_result(i)
        #print(number)
        if number == 'number7':
            correct_seven_output += 1
        seven_images += 1

    eight_images = 0
    correct_eight_output = 0
    for i in images['number8']:
        number = check_result(i)
        #print(number)
        if number == 'number8':
            correct_eight_output += 1
        eight_images += 1

    nine_images = 0
    correct_nine_output = 0
    for i in images['number9']:
        number = check_result(i)
        #print(number)
        if number == 'number9':
            correct_nine_output += 1
        nine_images += 1

    print(
        f'A {correct_zero_output * 100 / zero_images}% in number zero images ({zero_images} images, {correct_zero_output} correct)')
    print(
        f'A {correct_one_output * 100 / one_images}% in number one images ({one_images} images, {correct_one_output} correct)')
    print(
        f'A {correct_two_output * 100 / two_images}% in number two images ({two_images} images, {correct_two_output} correct)')
    print(
        f'A {correct_three_output * 100 / three_images}% in number three images ({three_images} images, {correct_three_output} correct)')
    print(
        f'A {correct_four_output * 100 / four_images}% in number four images ({four_images} images, {correct_four_output} correct)')
    print(
        f'A {correct_five_output * 100 / five_images}% in number five images ({five_images} images, {correct_five_output} correct)')
    print(
        f'A {correct_six_output * 100 / six_images}% in number six images ({six_images} images, {correct_six_output} correct)')
    print(
        f'A {correct_seven_output * 100 / seven_images}% in number seven images ({seven_images} images, {correct_seven_output} correct)')
    print(
        f'A {correct_eight_output * 100 / eight_images}% in number eight images ({eight_images} images, {correct_eight_output} correct)')
    print(
        f'A {correct_nine_output * 100 / nine_images}% in number nine images ({nine_images} images, {correct_nine_output} correct)')


images = load_images()
#print(images.get('five'))
#print(len(images['number5']))
#create_weights()
#learn(images)
check_accuracy(images)
