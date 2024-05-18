class Perceptron:

    def __init__(self, *, output):
        self.__output = output
        self.__incoming_perceptrons = []
        self.__outgoing_perceptrons = []
        self.__bias = 1
        self.__bias_weight = 0
        self.__delta = 0

    def get_output(self):
        return self.__output

    def get_incoming_perceptrons(self):
        return self.__incoming_perceptrons

    def get_outgoing_perceptrons(self):
        return self.__outgoing_perceptrons

    def get_bias(self):
        return self.__bias

    def get_bias_weight(self):
        return self.__bias_weight

    def get_delta(self):
        return self.__delta

    def set_bias_weight(self, bias_weight):
        self.__bias_weight = bias_weight

    def set_output(self, output):
        self.__output = output

    def set_incoming_perceptrons(self, incoming_perceptrons):
        self.__incoming_perceptrons = incoming_perceptrons

    def set_outgoing_perceptrons(self, outgoing_perceptrons):
        self.__outgoing_perceptrons = outgoing_perceptrons

    def set_bias(self, bias):
        self.__bias = bias

    def set_delta(self, delta):
        self.__delta = delta

    def __str__(self):
        return (f'Value: {self.__output.get_value()} Weight: {self.__output.get_weight()}, '
                f'Incoming Perceptrons: {len(self.__incoming_perceptrons)}, '
                f'Outgoing Perceptrons: {len(self.__outgoing_perceptrons)}')
