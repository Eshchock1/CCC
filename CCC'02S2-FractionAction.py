from math import *
num1 = int(input())
num2 = int(input())

lower = num1
higher = num2

if num1 > num2:
    higher = num1
    lower = num2


def findGCF(low, high):
    for i in range(low):
        factor = low - i
        if low % factor == 0 and high % factor == 0:
            return factor


gcf = findGCF(lower, higher)


def reduce(number1, number2, factor):
    if number1 == 0:
        print(0)
    elif number1 == number2:
        print(1)
    elif number1 < number2:
        print(str(int(number1 / factor)) + "/" + str(int(number2 / factor)))
    elif number1 > number2:
        number1 /= factor
        number2 /= factor
        wholeNumber = floor(number1/number2)
        remainder = number1 % number2
        if remainder == 0:
            print(wholeNumber)
        else:
            print(str(int(wholeNumber)) + " " + str(int(remainder)) + "/" + str(int(number2)))

reduce(num1, num2, gcf)