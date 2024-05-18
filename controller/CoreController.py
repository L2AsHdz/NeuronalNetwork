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
                print('Creating network...')
                input('Press Enter to continue...')

            elif option == "2":
                print('')

                if len(self.__model.get_layers()) == 0:
                    print('The network has not been created yet')
                else:
                    print('Netowrk...')

                input('Press Enter to continue...')

            elif option == "3":
                print('')

                if len(self.__model.get_layers()) == 0:
                    print('The network has not been created yet')
                else:
                    print('Training...')

                input('Press Enter to continue...')

            elif option == "4":
                print('')

                if len(self.__model.get_layers()) == 0:
                    print('The network has not been created yet')
                else:
                    print('Testing...')

                input('Press Enter to continue...')

            elif option == "0":
                self.__view.goodbye()
                input('Press Enter to continue...')
                exit()
            else:
                self.__view.invalid_option()
