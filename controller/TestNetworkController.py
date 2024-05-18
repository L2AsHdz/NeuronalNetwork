from service.NeuronalService import NeuronalService
from view.TestNetworkView import TestNetworkView


class TestNetworkController:

    def __init__(self, network):
        self.__network = network
        self.__view = TestNetworkView()
        self.__service = NeuronalService(neuronal_network=network)

    def run(self):
        self.__view.show(number_of_inputs=len(self.__network.get_layers()[0].get_perceptrons()))
        inputs = self.__view.get_inputs()
        self.__network.set_inputs(inputs)
        self.__service.execute()
        print(self.__network.print_final_layer_values())
        self.__view.print_success()
