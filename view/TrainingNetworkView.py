import os

from model.TrainingSet import TrainingSet


class TrainingNetworkView:

    def __init__(self):
        self.__training_sets = []


    def show(self):
        os.system('clear')
        print('Training Network')
        number_of_training_sets = int(input('How many training sets do you want to add? '))

        for i in range(number_of_training_sets):
            training_set = TrainingSet()
            print('Training set ', i + 1)
            input_values = (input('Enter inputs separated by commas: '))
            output_values = (input('Enter outputs separated by commas: '))
            training_set.set_input(list(map(float, input_values.split(','))))
            training_set.set_output(list(map(float, output_values.split(','))))
            self.__training_sets.append(training_set)

    def print_success_message(self):
        print('Neural network training successfully completed')

    def get_training_sets(self):
        return self.__training_sets
