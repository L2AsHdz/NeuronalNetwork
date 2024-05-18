class TestNetworkView:

    def __init__(self):
        self.__inputs = []

    def show(self, *, number_of_inputs):
        print('Test Network')
        self.__inputs = [float(input(f'Enter input {i+1}: ')) for i in range(number_of_inputs)]

    def print_success(self):
        print('Network tested successfully')

    def get_inputs(self):
        return self.__inputs
