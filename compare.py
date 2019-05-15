from sys import argv
script, first, second = argv

## Check if strings are equal
if first == second:
    print('The strings are both the same')
else:
    print('The strings are different')

## Check if first three characters are the same
if first[:3] == second[:3]:
    print('The first three characters are the same')
else:
    print('The first three characters are not the same')
