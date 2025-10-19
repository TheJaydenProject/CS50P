name = input('What\'s your name? ')


# inefficient way of doing this (imagine there was way more names)
if name == 'Harry' or name == 'Hermione' or name == 'Ron':
  print('Gryffindor')
elif name == 'Draco':
  print('Slytherin')
else:
  print('Who? ')  


# use match function instead
match name:
  case 'Harry' | 'Hermione' | 'Ron':
    print('Gryffindor')
  case 'Draco':
    print('Slytherin')
  # catch everything else
  case _:
    print('Who? ')
  