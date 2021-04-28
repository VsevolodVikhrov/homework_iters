import itertools


class Permutations:
    def __init__(self, string):
        self.__string = string
        self.__permuts = self.__permutations(self.__string)

    @staticmethod
    def __permutations(string):
        string = itertools.permutations(string, r=len(string))
        string = list(string)
        string = ["".join(i) for i in string]
        return string

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__permuts):
            raise StopIteration
        element = self.__permuts[self.__index]
        self.__index += 1
        return element


user_string = input("Input here your string: ")
a = Permutations(user_string)
for j in a:
    print(j)


