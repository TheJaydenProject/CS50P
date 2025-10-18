def main():
  hello()
  name = input('What\'s your name? ')
  hello(name)

# passing name variable value from main function to the hello function, so hello function can use it

# assign default value to 'to' in case input doesnt call hello() function with an argument
def hello(to='World'):
  print(f'Hello, {to}')

# Call Main function
main()