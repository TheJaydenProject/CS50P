def main():
  number = get_number()
  meow(number)


def get_number():
  # Loop till n more than 0 (Positive integer)
  while True:
    n = int(input('How many meows? '))
    if n > 0:
      break
  return n

# Loop n times
def meow(n):
  for _ in range(n):
    print('Meow')

# call main
main()