#Resolver equação do segundo grau
'''
print('Escreva a equação')
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b**2 - 4 * a * c

x1 = (-b + (delta)**(1/2)) / 2 * a
x2 = (-b - (delta)**(1/2)) / 2 * a

print(x1, x2)
'''
def coefA(str):
    if str == 'x²':
        return 1.0
    else:
        a = str.split('x')
        return float(a[0])
    
    
def coefB(str):
    if str == 'x':
        return 1.0
    else:
        b = str.split('x')
        return float(b[0])
    
def balancedEquation(equation): #Not = 0
    if 'x²' in equation[-1]:
        count = equation.count('x²')
        if count == 1:
            a = coefA(equation[-1])
            if equation[-2] == '+':
                b = coefB(equation[-3])
            else:
                b = coefB(equation[-3]) * -1
            if equation[-4] == '+':
                c = equation[-5]
                c = float(c)
            else:
                c = equation[-5]
                c = float(c) * -1
        elif count == 2:
            equation[-1] = equation[-1].split('x²')
            equation[-1] = equation[-1][0]
        else:
            pass
    elif 'x' in equation[-1]:
        equation[-1] = equation[-1].split('x')
        equation[-1] = equation[-1][0]
    else:
        pass
    return coefQuadratica(equation)
    
    

#Dada a equação quadrática, resolve-la
def coefQuadratica(equation):
    if '=' not in equation:
        print('Equação inválida')
        exit()
    a = 0
    b = 0
    c = 0
        
    #Separar a equação em uma lista para facilitar a manipulação e análise
    equation = equation.split(' ')
    #Caso tenha um espaço em -a se a for negativo
    if equation[0] == '-': equation[0] + equation[1]
    if len(equation) < 7:
        pass
    
    elif len(equation) == 7:
        if equation[-1] == '0': #Teste de equação balanceada
            a = coefA(equation[0])
            if equation[1] == '+':
                b = coefB(equation[2])
            else:
                b = coefB(equation[2]) * -1
            if equation[3] == '+':
                c = equation[4]
                c = float(c)
            else:
                c = equation[4]
                c = float(c) * -1
        else:
            balancedEquation(equation)
    else: #Equação grande
        pass 
    return(f'a = {a}, b = {b}, c = {c}')

print(coefQuadratica('- 4x + 1 = 2x²'))


