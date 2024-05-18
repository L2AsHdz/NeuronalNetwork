from controller.CreateNetworkController import CreateNetworkController
from controller.TestNetworkController import TestNetworkController
from controller.TrainingNetworkController import TrainingNetworkController
from model.NeuronalNetwork import NeuronalNetwork
from view.MainView import MainView


class CoreController:

    def __init__(self):
        self.__view = MainView()
        self.__model = NeuronalNetwork(layers=[])

    def run(self):
        option = -1

        while option != 0:
            self.__view.show()

            option = self.__view.get_option()

            if option == "1":
                create_network_controller = CreateNetworkController(network=self.__model)
                create_network_controller.run()
                input('Press Enter to continue...')

            elif option == "2":
                print('')

                if len(self.__model.get_layers()) == 0:
                    print('The network has not been created yet')
                else:
                    print(self.__model)

                input('Press Enter to continue...')

            elif option == "3":
                print('')

                if len(self.__model.get_layers()) == 0:
                    print('The network has not been created yet')
                else:
                    training_controller = TrainingNetworkController(network=self.__model)
                    training_controller.run()

                input('Press Enter to continue...')

            elif option == "4":
                print('')

                if len(self.__model.get_layers()) == 0:
                    print('The network has not been created yet')
                else:
                    test_network_controller = TestNetworkController(network=self.__model)
                    test_network_controller.run()

                input('Press Enter to continue...')

            elif option == "0":
                self.__view.goodbye()
                input('Press Enter to continue...')
                exit()
            else:
                self.__view.invalid_option()
