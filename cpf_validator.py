import re

#--------------------------------------------
# CPF validation with lambda (shortest code)
#--------------------------------------------
class CpfValidator:

    def isValid(self, number):

        # invalid length or repeated digits
        if len(number) != 11 or re.search(r"(\d)(\1{10})", number): return False
        # if len(number) != 11 or number == str(number[0]) * len(number): return False  # ALTERNATIVE TEST without regex

        for i in reversed(range(1, 3)):
            digit = sum(map(lambda e: e[0] * int(e[1]), enumerate(reversed(list(number[:-i])), start = 2))) % 11
            if int(number[-i]) != (0 if digit < 3 else 11 - digit): return False

        return True



#--------------------------------------------
# CPF validation
#--------------------------------------------
class CpfValidator1:

    def isValid(self, number):

        # invalid length or repeated digits
        if len(number) != 11 or re.search(r"(\d)(\1{10})", number): return False
        # if len(number) != 11 or number == str(number[0]) * len(number): return False  # ALTERNATIVE TEST without regex

        for cycle in range(2):

            limitIndex = 9 if cycle == 0 else 10
            baseWeight = limitIndex + 1
            temp = 0

            for index in range(0, limitIndex):
                temp += int(number[index]) * (baseWeight - index)

            temp %= 11
            digit = 0 if temp < 2 else 11 - temp

            if digit != int(number[limitIndex]):
                return False

        return True

#--------------------------------------------
# CPF validation with comprehension list
#--------------------------------------------
class CpfValidator2:

    def isValid(self, number):

        # invalid length or repeated digits
        if len(number) != 11 or re.search(r"(\d)(\1{10})", number): return False
        # if len(number) != 11 or number == str(number[0]) * len(number): return False  # ALTERNATIVE TEST without regex

        for cycle in range(2):

            limitIndex = 11 if cycle == 0 else 12
            cpf = list(number[: limitIndex - 2])

            digit = sum([int(x) * y for x, y in zip(cpf, [n for n in reversed(range(1, limitIndex))])]) % 11
            digit = 0 if temp < 2 else 11 - temp

            if digit != int(number[limitIndex - 2]): return False

        return True

# main

cpfValidator = CpfValidator()

while True:

    print()
    print("-"*41)
    print("Enter the CPF digits     [type X to exit]")
    print("-"*41)

    cpf = input("? ")
    if cpf.upper() == "X": break

    print("\nCPF is " + ("valid!" if cpfValidator.isValid(cpf) else " I N V A L I D  !!!"))
