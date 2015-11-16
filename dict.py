__author__='kiran'
spanish=dict()
spanish['a']='Apple'
spanish['b']='Bat'

print("Dictionary",spanish)

numberFormat = "Count in Spanish: {one}, {two}, {three}, ..."
withSubstitutions = numberFormat.format(one='uno', two='dos', three='tres')
print(withSubstitutions)
#print("Dictionary",**spanish)
print("local dictionary values",locals())