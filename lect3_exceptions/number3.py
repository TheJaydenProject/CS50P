# pass function
# pass when exception is caught
def main ():
  number = get_int('What\'s x? ')
  print(f'x is {number}')

def get_int(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      pass

main()