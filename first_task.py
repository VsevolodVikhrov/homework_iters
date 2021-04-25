class GetLiteralNum:
    __literals = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }

    def __init__(self, numbers):
        self.__numbers = numbers
        self.__numbers_with_literals = []

    def get_literal(self):
        for i in self.__numbers:
            list_of_literals = ""
            for j in i:
                list_of_literals = list_of_literals + f"{self.__literals[j]} "
            self.__numbers_with_literals.append(f"{i} - {list_of_literals}")
        return self

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__numbers):
            raise StopIteration
        element = self.__numbers_with_literals[self.__index]
        self.__index += 1
        return element


def get_user_input():
    list_of_user_input = []
    user_input = input("Enter numbers string: ")
    user_input = user_input.split()
    for i in user_input:
        if i.isdigit():
            list_of_user_input.append(i)
    get_next_element(list_of_user_input)


def get_next_element(list_of_user_input):
    data_iter = GetLiteralNum(list_of_user_input).get_literal()
    for i in data_iter:
        print(i)


if __name__ == '__main__':
    get_user_input()
