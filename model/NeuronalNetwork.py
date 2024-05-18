class NeuronalNetwork:

    def __init__(self, *, layers):
        self.__layers = layers
        self.__learning_rate = 0.3
        self.__training_epochs = 10000
        self.__threshold = 0.05
        self.__activation_function_hidden_layers = 0
        self.__activation_function_output_layer = 0

    def get_layers(self):
        return self.__layers

    def get_learning_rate(self):
        return self.__learning_rate

    def get_training_epochs(self):
        return self.__training_epochs

    def get_threshold(self):
        return self.__threshold

    def get_activation_function_hidden_layers(self):
        return self.__activation_function_hidden_layers

    def get_activation_function_output_layer(self):
        return self.__activation_function_output_layer

    def set_layers(self, layers):
        self.__layers = layers

    def set_learning_rate(self, learning_rate):
        self.__learning_rate = learning_rate

    def set_training_epochs(self, training_epochs):
        self.__training_epochs = training_epochs

    def set_activation_function_hidden_layers(self, activation_function_hidden_layers):
        self.__activation_function_hidden_layers = activation_function_hidden_layers

    def set_activation_function_output_layer(self, activation_function_output_layer):
        self.__activation_function_output_layer = activation_function_output_layer

    def set_threshold(self, threshold):
        self.__threshold = threshold

    def set_inputs(self, inputs):
        layers = self.__layers

        for index, perceptron in enumerate(layers[0].get_perceptrons()):
            perceptron.get_output().set_value(inputs[index])

    def print_final_layer_values(self):
        result = ''
        for index, perceptron in enumerate(self.__layers[-1].get_perceptrons()):
            result += f'\nOutput {index+1}: {perceptron.get_output().get_value()}'
        return result

    def __str__(self):

        result = f'''Learning Rate: {self.__learning_rate}
Training Epochs: {self.__training_epochs}
Activation Function Hidden Layers: {self.__activation_function_hidden_layers}
Activation Function Output Layer: {self.__activation_function_output_layer}
Layers: {len(self.__layers)}
'''
        result += '\n'.join([str(layer) for layer in self.__layers])
        return result
