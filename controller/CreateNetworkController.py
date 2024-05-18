import random

from model.Layer import Layer
from model.Output import Output
from model.Perceptron import Perceptron
from model.enum.LayerType import LayerType
from view.CreateNetworkView import CreateNetworkView


class CreateNetworkController:

    def __init__(self, *, network):
        self.__network = network
        self.__view = CreateNetworkView()

    def run(self):
        self.__view.show()

        self.__network.set_layers([])

        # creating input layer
        self.create_layer(self.__view.get_number_of_inputs(), LayerType.INPUT)

        # creating hidden layers
        for i in range(self.__view.get_number_of_hidden_layers()):
            self.create_layer(self.__view.get_number_of_neurons_per_layer()[i], LayerType.HIDDEN)

        # creating output layer
        self.create_layer(self.__view.get_number_of_outputs(), LayerType.OUTPUT)

        # creating connections between layers
        self.create_connections()

        # setting parameters
        self.__network.set_activation_function_hidden_layers(self.__view.get_activation_function_hidden_layers())
        self.__network.set_activation_function_output_layer(self.__view.get_activation_function_output_layer())

        self.__view.print_success()

    def create_layer(self, number_of_neurons, layer_type):
        input_layer = Layer(layer_type=layer_type, perceptrons=[])

        for i in range(number_of_neurons):
            weight = round(random.uniform(-1, 1), 2)
            output = Output(weight=weight)
            perceptron = Perceptron(output=output)
            weight = round(random.uniform(-1, 1), 2)
            perceptron.set_bias_weight(weight)
            input_layer.get_perceptrons().append(perceptron)

        self.__network.get_layers().append(input_layer)

    def create_connections(self):
        for index, current_layer in enumerate(self.__network.get_layers()):
            previous_layer = None
            next_layer = None
            if current_layer.get_layer_type() == LayerType.INPUT or current_layer.get_layer_type() == LayerType.HIDDEN:
                next_layer = self.__network.get_layers()[index + 1]

                for perceptron in current_layer.get_perceptrons():
                    perceptron.set_outgoing_perceptrons(next_layer.get_perceptrons())

            if current_layer.get_layer_type() == LayerType.HIDDEN or current_layer.get_layer_type() == LayerType.OUTPUT:
                previous_layer = self.__network.get_layers()[index - 1]

                for perceptron in current_layer.get_perceptrons():
                    perceptron.set_incoming_perceptrons(previous_layer.get_perceptrons())

        # for i in range(1, len(self.__network.get_layers())):
        #     current_layer = self.__network.get_layers()[i]
        #     previous_layer = self.__network.get_layers()[i - 1]
        #
        #     for perceptron in current_layer.get_perceptrons():
        #         perceptron.set_incoming_perceptrons(previous_layer.get_perceptrons())
