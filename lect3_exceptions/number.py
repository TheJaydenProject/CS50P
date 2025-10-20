# What if input is not an int()
# Catch Errors Solution

def main ():
  number = get_int()
  print(f'x is {number}')

# Catch Errors Solution
def get_int():
  while True:
    try:
      x =int(input('What\'s x? '))
    except ValueError:
      print('x is not an integer')
    # else: to run after try: if there are no exceptions
    # why else:? 
    # if else: is not written, when an exception is caught, x will no longer be defined leading to a NameError
    else:
      # return function breaks out of the loop and returns a variable/value 
      # dont need to use break if using return
      return x

main()


