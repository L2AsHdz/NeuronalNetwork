import numpy as np

from model.TrainingSet import TrainingSet
from model.enum.ActivationFunctionType import ActivationFunctionType
from model.enum.LayerType import LayerType
from service.NeuronalService import NeuronalService
from view.TrainingNetworkView import TrainingNetworkView


class TrainingNetworkController:

    def __init__(self, *, network):
        self.__network = network
        self.__view = TrainingNetworkView()
        self.__service = NeuronalService(neuronal_network=network)
        self.__mean_square_error = lambda y, o: np.mean((y - o) ** 2)
        self.__sigmoid = lambda x: 1 / (1 + np.exp(-x))
        self.__tanh = lambda x: np.tanh(x)
        self.__sigmoid_derivative = lambda x: self.__sigmoid(x) * (1 - self.__sigmoid(x))
        self.__tanh_derivative = lambda x: 1 - np.tanh(x) ** 2
        self.__step_derivative = lambda x: 0
        self.__identity_derivative = lambda x: 1

    def run(self):
        self.__view.show()

        training_sets = self.__view.get_training_sets()
        # training1 = TrainingSet()
        # training1.set_input([0, 0])
        # training1.set_output([1])
        #
        # training2 = TrainingSet()
        # training2.set_input([0, 1])
        # training2.set_output([0])
        #
        # training3 = TrainingSet()
        # training3.set_input([1, 0])
        # training3.set_output([0])
        #
        # training4 = TrainingSet()
        # training4.set_input([1, 1])
        # training4.set_output([1])
        # training_sets = [training1, training2, training3, training4]

        invalid_error_threshold = True

        iteration = 0
        while iteration < self.__network.get_training_epochs():
            error_sum = 0
            print(f'Iteration: {iteration}')
            for training_set in training_sets:
                print(training_set)
                self.__network.set_inputs(training_set.get_input())
                self.__service.execute()

                output_values = [perceptron.get_output().get_value() for perceptron in
                                 self.__network.get_layers()[-1].get_perceptrons()]

                mse = self.__mean_square_error(np.array(training_set.get_output()), np.array(output_values))
                print(f'Expected: {training_set.get_output()}, Output: {output_values}, MSE: {mse}')
                error_sum += mse
                if mse < self.__network.get_threshold():
                    invalid_error_threshold = False
                    break

                # Backpropagation
                learning_rate = self.__network.get_learning_rate()
                for index_layer, layer in enumerate(reversed(self.__network.get_layers()[1:])):
                    print(f'Updating weights for layer {index_layer+1} - {layer.get_layer_type()}')
                    for index, perceptron in enumerate(layer.get_perceptrons()):
                        predicted_output = perceptron.get_output().get_value()

                        # Calculate error
                        error = 0
                        if layer.get_layer_type() == LayerType.OUTPUT:
                            expected_output = training_set.get_output()[index]
                            error = expected_output - predicted_output
                        else:
                            # Calcular el error acumulado de la siguiente capa
                            outgoing_perceptrons = perceptron.get_outgoing_perceptrons()
                            error = sum(perceptron.get_output().get_weight() * next_perceptron.get_delta()
                                        for next_perceptron in outgoing_perceptrons)

                        # Calculate delta error
                        d_error = 0
                        activation_function = self.__network.get_activation_function_hidden_layers() if (
                                layer.get_layer_type() == LayerType.HIDDEN.value) else (
                            self.__network.get_activation_function_output_layer())

                        if activation_function == ActivationFunctionType.SIGMOID.value:
                            d_error = error * self.__sigmoid_derivative(predicted_output)
                        elif activation_function == ActivationFunctionType.TANH.value:
                            d_error = error * self.__tanh_derivative(predicted_output)
                        elif activation_function == ActivationFunctionType.STEP.value:
                            d_error = error * self.__step_derivative(predicted_output)
                        elif activation_function == ActivationFunctionType.IDENTITY.value:
                            d_error = error * self.__identity_derivative(predicted_output)

                        # Save delta error
                        perceptron.set_delta(d_error)

                        # Update weights
                        perceptron.set_bias_weight(perceptron.get_bias_weight() + learning_rate * d_error)

                        incoming_perceptrons = perceptron.get_incoming_perceptrons()
                        for incoming_perceptron in incoming_perceptrons:
                            incoming_perceptron.get_output().set_weight(
                                incoming_perceptron.get_output().get_weight() + learning_rate * d_error
                                * incoming_perceptron.get_output().get_value())

            iteration += 1
            print(f'Error: {error_sum}')
            print('')

        self.__view.print_success_message()
