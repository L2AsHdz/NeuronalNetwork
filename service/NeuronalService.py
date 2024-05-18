import numpy as np

from model.enum.ActivationFunctionType import ActivationFunctionType
from model.enum.LayerType import LayerType


class NeuronalService:

    def __init__(self, *, neuronal_network):
        self.__neuronal_network = neuronal_network
        self.__sigmoid = lambda x: 1 / (1 + np.exp(-x))
        self.__tanh = lambda x: np.tanh(x)
        self.__step = lambda x: 1 if x > 0 else 0
        self.__identity = lambda x: x

    def execute(self):
        layers = self.__neuronal_network.get_layers()

        for index in range(1, len(layers)):
            layer = layers[index]
            for perceptron in layer.get_perceptrons():
                weighted_sum = 0

                incoming_perceptrons = perceptron.get_incoming_perceptrons()
                for incoming_perceptron in incoming_perceptrons:
                    weighted_sum += incoming_perceptron.get_output().get_result()

                weighted_sum += perceptron.get_bias() * perceptron.get_bias_weight()

                output_value = 0
                activation_function = self.__neuronal_network.get_activation_function_hidden_layers() if (
                        layer.get_layer_type() == LayerType.HIDDEN) else (
                        self.__neuronal_network.get_activation_function_output_layer())

                if activation_function == ActivationFunctionType.SIGMOID.value:
                    output_value = self.__sigmoid(weighted_sum)
                elif activation_function == ActivationFunctionType.TANH.value:
                    output_value = self.__tanh(weighted_sum)
                elif activation_function == ActivationFunctionType.STEP.value:
                    output_value = self.__step(weighted_sum)
                elif activation_function == ActivationFunctionType.IDENTITY.value:
                    output_value = self.__identity(weighted_sum)

                perceptron.get_output().set_value(output_value)
