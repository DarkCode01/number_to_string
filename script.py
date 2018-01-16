#! /usr/bin/env python3

import sys
from termcolor import colored
from numeros_ import LISTA_NUMEROS, NUMEROS_RAROS


class NumberToString(object):

    def __init__(self, number):
        self.result = ""
        self.number_copy = number
        self.number = number.split(",")
        self.len_ = len(self.number)
        self.number = [n.replace(" ", "") for n in self.number]
        self.LN = LISTA_NUMEROS
        self.len_group = ""

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
                return (colored("Help", "white"), colored(fl.read(), "green"))

    def find(self):

        try:
            if len(self.number) == 0:
                return 0

            self.len_group = str(len(self.number[0]))
            for i, num in enumerate(self.number[0]):
                if int(self.len_group) == 2 and \
                   int("".join(self.number[0][i:])) in NUMEROS_RAROS:

                    tmp = int("".join(self.number[0][i:]))
                    self.result += self.LN["1"][tmp - 1]
                    self.result += " "
                    break
                else:
                    if int(num) >= 1:
                        self.result += self.LN[self.len_group][int(num) - 1]
                        self.result += " "
                        if self.len_group == "2" and self.number[0][i+1] != "0":
                            self.result += "y " 

                self.len_group = int(self.len_group) - 1
                self.len_group = str(self.len_group)

            if self.len_ > 1 and int(self.number[0]) > 0:
                self.result += self.LN["4"][self.len_ - 2]
                self.result += ", "

            self.len_ -= 1
            self.number.pop(0)
            self.find()
            return (colored(self.number_copy, "red"),
                    colored(self.result, "green"))

        except KeyError as e:
            return self.help(e)


if __name__ == "__main__":
    try:
        new = NumberToString(sys.argv[1])
        num, string = new.find()
        print(num, " -> ", string)
    except Exception as e:
        print(colored("\t script 1215, Falto el numero", "red"))
        print(e)

