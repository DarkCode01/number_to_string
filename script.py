#! /usr/bin/env python3
"""
    This is a module capable of returning the amount of a number
    literally.
"""
import sys
from termcolor import colored
from numeros_ import LISTA_NUMEROS, NUMEROS_RAROS


class NumberToString(object):
    """
        This is a module capable of returning the amount of a number
        literally.

        This module is for educational purposes, is developed based on
        recursion looking for a simple and friendly way for people who
        are beginning to learn python.

        example:
        >>> input ("1,000,000")
        >>> output: "(uno|un) millon(es)"

        Note: The number entered must be separated with commas.
    """

    def __init__(self, number=None):
        if number:
            self.result = ""
            self.number_copy = number
            self.number = number.split(",")
            self.len_ = len(self.number)
            self.number = [n.replace(" ", "") for n in self.number]
            self.LN = LISTA_NUMEROS
            self.vueltas = len(self.number)
            self.len_group = ""
        pass

    def help(self, e=None):
        if e:
            e = """
                 Posibles errores:
                  {0}
                  {1}
                 Info:
                  {2}
                  {3}
            """.format(
                colored("-El numero ingresado no es soportado", "red"),
                colored("-El numero contiene caracteres extranos", "red"),
                colored("-Debes separarcon una (,) las unidades", "yellow"),
                colored("-Se retornara una tupla (num, cantidad)", "yellow")
            )
            return (colored("", "white"), e)
        else:
            with open("man.txt", "r") as fl:
                return (colored("Help", "white"), colored(fl.readlines(), "green"))

    def find(self):
        """
            This metidi will take care of returning a tuple that will
            contain the number that had been entered and the amount literally.

            Example:
                (1,000, "(uno|un) mil") -> Tuple returned
                    ^            ^
                    |            |
                self.number | self.result
                |\
                (Number entered)
        """

        try:
            if len(self.number) == 0:
                return self.result

            self.len_group = str(len(self.number[0]))
            for i, num in enumerate(self.number[0]):
                if int(self.len_group) == 2 and \
                   int("".join(self.number[0][i:])) in NUMEROS_RAROS:

                    tmp = int("".join(self.number[0][i:]))
                    self.result += self.LN["1"][tmp - 1]
                    self.result += " "
                    break
                else:
                    if int(num) == 1 and self.len_ == 2:
                        pass
                    elif int(num) >= 1:
                        self.result += self.LN[self.len_group][int(num) - 1]
                        self.result += " "
                        self.result += "y " if int(self.len_group) == 2 else ""

                self.len_group = int(self.len_group) - 1
                self.len_group = str(self.len_group)

            if self.len_ > 1 and int(self.number[0]) > 0:
                self.result += self.LN["4"][self.len_ - 2]
                self.result += ", "

            self.len_ -= 1
            self.vueltas -= 1
            self.number.pop(0)
            self.find()
            return (colored(self.number_copy, "red"),
                    colored(self.result, "green"))

        except KeyError as e:
            return self.help(e)


if __name__ == "__main__":
    if sys.argv[1] == "--help":
        new = NumberToString()
        title, text = new.help()
        print(title, ": \n\t", text)
    elif sys.argv[1]:
        new = NumberToString(sys.argv[1])
        num, string = new.find()
        print(num, " -> ", string)
