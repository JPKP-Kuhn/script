import math, sympy
#sympy for simbolic and math for calculations

print(sympy.sqrt(17))
print(math.sqrt(17))

x = sympy.symbols('x')
y = sympy.symbols('y')

expression = 2 * x * y

print(expression)
print(sympy.frac(expression))

print(sympy.solve(2*x + 3, x))
