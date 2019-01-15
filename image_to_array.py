from PIL import Image
import numpy


class ImageToArray:
    """
    Classe com o único objetivo de receber um arquivo de imagem e retornar
    uma lista (vetor unidimensional) com valores 1 ou 0 correspondentes aos
    pixels da imagem, 0 são pixels pretos e qualquer pixel diferente de zero terá o valor 1

    Para entender a implementação mais a fundo é necessário ter conhecimento das
    bibliotecas utilizadas e talvez isso não seja necessário para ter conhecimento
    de como funciona o algoritmo de aprendizagem
    """

    def __init__(self, image_path):
        self.__image = image_path

    def get_array(self):
        image = Image.open(self.__image).convert('L')
        width, height = image.size
        greyscale_map = list(image.getdata())
        greyscale_map = numpy.array(greyscale_map)
        greyscale_map = greyscale_map.reshape((height,width))
        #print(greyscale_map.shape)
        greyscale_map[greyscale_map > 0] = 1
        return greyscale_map.flatten()
