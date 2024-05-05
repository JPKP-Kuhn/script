#function to count how many x², x and numbers are in the equation
def counting(equation):
    count = 0
    for i in equation:
        if 'x²' in i:
            count += 1
        elif 'x' in i:
            count += 1
        else:
            count += 1
    return count

print(counting(['x² + 2x + 4 = 0']))
equation = 'x² + 2x + 4 = 0'
print(equation.count('x²'))
print(' ')
print(equation.count('x'))

if equation.count('x²') > 1 or equation.count('x') > 2:
    print('Equação inválida')