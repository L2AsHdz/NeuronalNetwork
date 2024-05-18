class Output:

    def __init__(self, *, value=0, weight=0):
        self.__value = value
        self.__weight = weight

    def get_value(self):
        return self.__value

    def get_weight(self):
        return self.__weight

    def get_result(self):
        return self.__value * self.__weight

    def set_value(self, value):
        self.__value = value

    def set_weight(self, weight):
        self.__weight = weight

    def __str__(self):
        return "Output: " + str(self.__value) + " Weight: " + str(self.__weight)