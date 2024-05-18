class Layer:

    def __init__(self, *, layer_type, perceptrons):
        self.__layer_type = layer_type
        self.__perceptrons = perceptrons

    def get_layer_type(self):
        return self.__layer_type

    def get_perceptrons(self):
        return self.__perceptrons

    def set_layer_type(self, layer_type):
        self.__layer_type = layer_type

    def set_perceptrons(self, perceptrons):
        self.__perceptrons = perceptrons

    def __str__(self):
        result = f'''Layer Type: {self.__layer_type}
Perceptrons:
'''
        result += '\n'.join([str(perceptron) for perceptron in self.__perceptrons])
        return result
