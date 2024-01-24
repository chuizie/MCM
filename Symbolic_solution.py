from sympy.abc import x
from sympy import diff, dsolve, simplify, Function

y = Function('y')
eq = diff(y(x), x, 2) + 2 * diff(y(x), x) + 2 * y(x)  # 定义方程
con = {y(0): 0, diff(y(x), x).subs(x, 0): 1}  # 定义初值条件
y = dsolve(eq, ics=con)
print(simplify(y))


from sympy.abc import x  # 引进符号变量x
from sympy import Function, diff, dsolve, sin

y = Function('y')
eq = diff(y(x), x, 2) + 2 * diff(y(x), x) + 2 * y(x) - sin(x)  # 定义方程
con = {y(0): 0, diff(y(x), x).subs(x, 0): 1}  # 定义初值条件
y = dsolve(eq, ics=con)
print(y)


import sympy as sp

t = sp.symbols('t')
x1, x2, x3 = sp.symbols('x1,x2,x3', cls=sp.Function)
eq = [x1(t).diff(t) - 2 * x1(t) + 3 * x2(t) - 3 * x3(t),
      x2(t).diff(t) - 4 * x1(t) + 5 * x2(t) - 3 * x3(t),
      x3(t).diff(t) - 4 * x1(t) + 4 * x2(t) - 2 * x3(t)]
con = {x1(0): 1, x2(0): 2, x3(0): 3}
s = sp.dsolve(eq, ics=con)
print(s)