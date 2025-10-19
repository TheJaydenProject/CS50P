x = int(input('What\'s x? '))
y = int(input('What\'s y? '))

if x < y:
  print('x is less than y')
elif x > y:
  print('x is greater than y')
else:
  print('x is equal to y')



# Find out whether x is equal to y
if x < y or x > y:
  print('x does not equal to y')
else:
  print('x equals to y')

# More Simple Efficient
if x == y:
  print('x equals to y')
else:
  print('x does not equal to y')