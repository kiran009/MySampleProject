person = input('Enter your name: ')
greeting = 'Hello {person}!'.format(**locals())
print(greeting)