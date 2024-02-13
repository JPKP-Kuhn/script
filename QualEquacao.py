def grauEquacao(equacao):
    sobrescrito = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
    grau = 0
    for i in range(10):
        if sobrescrito[i] in equacao:
            grau = i      
    if grau == 0:
        print('A equação não é de grau 1')
        return grau
    else:    
        print('O grau da equação é: ', grau)
        return grau

grauEquacao('x² + 2x⁵ + 1')
