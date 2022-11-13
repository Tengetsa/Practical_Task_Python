
from random import randint

def coefficients_polynomial_list(length, max_coeffs):
    my_list = []
    for i in range(length):
        my_list.append(randint(0, max_coeffs))
    return my_list

def Print_power_equation(coeffs):
    coeff_section = ''
    for i in range (len(coeffs) - 1, 0, -1):
        if coeffs[i] != 0:
            if i == 1:
                coeff_section += f'{coeffs[i]}x + '
            else:
                coeff_section += f'{coeffs[i]}x^{i} + '
    if coeffs[i] == 0:
        coeff_section += ' = 0'
    else:
        coeff_section += f'{coeffs[0]} = 0'
    return coeff_section