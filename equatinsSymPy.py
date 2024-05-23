import math, sympy
#sympy for simbolic and math for calculations

print(sympy.sqrt(17))
print(math.sqrt(17))

variable = sympy.symbols('x')
y = sympy.symbols('y')

expression = 2 * variable * y

print(expression)
print(sympy.frac(expression))

a = 2
b = 3
c = 0
print(sympy.solve(sympy.Eq(a*variable+b, c)))

print(sympy.solve(sympy.Eq(2*variable + 3*variable + 4 - 2, variable)))

print(sympy.solve(sympy.Eq(a*variable+b, c)))
