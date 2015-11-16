colors=['red', 'green', 'blue']
[1, 3, 5, 7, 9, 11]
['silly', 57, 'mixed', -23, 'example']
[] # the empty list
ran=list(range(1000))
print("Colours is",colors)
print("Range is",ran)
for count in [1,2,3]:
    print(count)
    print('Yes'*count)
for cue in ['animal', 'food', 'city']:
    print("Cue is",'\t', cue.capitalize(),'\n')
for i in range(10):
    j=10-i
    #print("J value is:",j,"I value is:",i)
    #print("J value is",j)
    print('Hello'*i+'Hello'*j)