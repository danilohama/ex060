""" Faça um programa que leia um número qualquer e mostre o seu fatorial
ex: 5! = 5x4x3x2x1= 120
"""
#  from math import factorial
# n = int(input('Digite um número para calcular seu fatorial: '))
# f = factorial(n)
# print('O factorial de \033[33m{}\033[0m é \033[33m{}\033[0m'.format(n, f))
from time import sleep

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('\033[33mCalculando\033[0m {}! = '.format(n), end='')
sleep(2)
while c > 0:
    print('\033[33m{}\033[0m'.format(c), end='')
    print(' \033[37mx\033[0m ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('\033[32m{}\033[0m'.format(f))
