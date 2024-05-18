import os
from time import sleep


class CreateNetworkView:

    def __init__(self):
        self.__number_of_inputs = 0
        self.__number_of_outputs = 0
        self.__number_of_hidden_layers = 0
        self.__number_of_neurons_per_layer = []
        self.__activation_function_hidden_layers = 0
        self.__activation_function_output_layer = 0

    def show(self):
        os.system('clear')
        print('Create Network')
        self.__number_of_inputs = int(input('Enter the number of inputs: '))
        self.__number_of_outputs = int(input('Enter the number of outputs: '))
        self.__number_of_hidden_layers = int(input('Enter the number of hidden layers: '))

        for i in range(self.__number_of_hidden_layers):
            self.__number_of_neurons_per_layer.append(
                int(input(f'Enter the number of neurons for hidden layer {i + 1}: ')))

        print('Select the activation function for hidden layers')
        print('1. Sigmoid')
        print('2. Tanh')
        print('3. Step')
        print('4. Identity')
        self.__activation_function_hidden_layers = int(input('Enter an option: '))

        print('Select the activation function for the output layer')
        print('1. Sigmoid')
        print('2. Tanh')
        print('3. Step')
        print('4. Identity')
        self.__activation_function_output_layer = int(input('Enter an option: '))

    def print_success(self):
        print('Network created successfully')

    def get_number_of_inputs(self):
        return self.__number_of_inputs

    def get_number_of_outputs(self):
        return self.__number_of_outputs

    def get_number_of_hidden_layers(self):
        return self.__number_of_hidden_layers

    def get_number_of_neurons_per_layer(self):
        return self.__number_of_neurons_per_layer

    def get_activation_function_hidden_layers(self):
        return self.__activation_function_hidden_layers

    def get_activation_function_output_layer(self):
        return self.__activation_function_output_layer
