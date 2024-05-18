import os
from time import sleep


class MainView:

    def __init__(self):
        self.__option = 0

    def show(self):
        os.system('clear')
        print('Neuronal Network')
        print('1. Create Network')
        print('2. Show Network')
        print('3. Train Network')
        print('4. Test Network')
        print('0. Exit')

        self.__option = input('Enter an option: \n')

    def goodbye(self):
        print('Goodbye....')

    def invalid_option(self):
        print('Invalid option')
        sleep(1)

    def get_option(self):
        return self.__option
