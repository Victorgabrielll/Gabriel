# Faça um programa,dado dois dados inteiros, positivos
# e distinto x e y,calcular o mdc de x e y

from math import gcd
#biblioteca que auxilia na equação do MDC
x = int(input('Digite o primeiro valor de x '))
y = int(input('Digite o segundo valor de y '))
print('O MDC(', x,',', y,') =',(gcd(x, y)))
#resultado final
