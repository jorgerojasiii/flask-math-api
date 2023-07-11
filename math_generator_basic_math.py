import mathgenerator
import random

#generate an addition problem
def question():
    randy = random.randint(0, 13)
    if randy == 0:
        category = 'absolute difference'
        problem, solution = mathgenerator.absolute_difference()
    if randy == 1:
        category = 'addition'
        problem, solution = mathgenerator.addition()
    if randy == 2:
        category = 'divide fractions'
        problem, solution = mathgenerator.divide_fractions()
    if randy == 3:
        category = 'division'
        problem, solution = mathgenerator.division()
    if randy == 4:
        category = 'factorial'
        problem, solution = mathgenerator.factorial()
    if randy == 5:
        category = 'multiplication'
        problem, solution = mathgenerator.fraction_multiplication()
    if randy == 6:
        category = 'greatest common divisor'
        problem, solution = mathgenerator.greatest_common_divisor()
    if randy == 7:
        category = 'is composite'
        problem, solution = mathgenerator.is_composite()
    if randy == 8:
        category = 'is prime'
        problem, solution = mathgenerator.is_prime()
    if randy == 9:
        category = 'multiplication'
        problem, solution = mathgenerator.multiplication()
    if randy == 10:
        category = 'power of powers'
        problem, solution = mathgenerator.power_of_powers()
    if randy == 11:
        category = 'square'
        problem, solution = mathgenerator.square()
    if randy == 12:
        category = 'square root'
        problem, solution = mathgenerator.square_root()
    if randy == 13:
        category = 'subtraction'
        problem, solution = mathgenerator.subtraction()

    return category, problem, solution

print(question())