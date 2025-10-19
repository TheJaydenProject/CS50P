def main():
  x = int(input('What\'s x? '))
  if is_even(x):
    print('x is even')
  else:
    print('x is odd')


# Beginner
def is_even(n):
  if n % 2 == 0:
    return True
  else:
    return False

# Compile into one line
def is_even(n):
  return True if n % 2 == 0 else False

# Shortest readable line
def is_even(n):
  return n % 2 == 0

main()