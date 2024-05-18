class TrainingSet:

    def __init__(self):
        self.__input = []
        self.__output = []

    def get_input(self):
        return self.__input

    def get_output(self):
        return self.__output

    def set_input(self, input):
        self.__input = input

    def set_output(self, output):
        self.__output = output

    def __str__(self):
        result = 'Inputs: '
        for i in self.__input:
            result += f'{i}, '

        result += 'Outputs: '
        for output in self.__output:
            result += f'{output}, '

        return result
