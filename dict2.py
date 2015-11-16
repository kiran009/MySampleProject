x = 20
y = 30
sum = x+y
prod = x*y
formatStr = '{x} + {y} = {sum}; {x} * {y} = {prod}.'
equations = formatStr.format(**locals())
print(equations)