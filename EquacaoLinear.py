#Resolver equações lineares
equation = input('Digite a equação: ')
if '=' not in equation:
    print('Equação inválida')
    exit()
#ax + b = c
equation = equation.split(' ')

def coefA(str):
    if str == 'x':
        return 1.0
    else:
        a = str.split('x')
        return float(a[0])
    
c = equation[-1]
c = float(c)
a = coefA(equation[0])

print(equation)
if equation[1] == '+':
    b = equation[2]
    b = float(b)
else:
    b = equation[2]
    b = float(b) * -1

x = (c - b) / a
print('O valor de x é: ', x)