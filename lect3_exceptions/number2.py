# What if input is not an int()
# Catch Errors Solution


# Could do this instead 
def main ():
  number = get_int('What\'s z? ')
  print(f'z is {number}')


def get_int(prompt):
  while True:
    try:
      x =int(input(prompt))
      # breaking out of the loop using return function right after int() input is valid
      return x
    except ValueError:
      print('Input is not an integer')

main()


# tighten further without defining a variable
def main2 ():
  number = get_int('What\'s x? ')
  print(f'x is {number}')

def get_int(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print('Input is not an integer')

main2()