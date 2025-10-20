def main():
  print_column(3)
  print_row(4)
  print()
  print_square(3)
  print()
  print_square2(3)
  print()
  print_square3(3)

def print_column(height):
  for _ in range(height):
    print('#')

def print_row(width):
  print('?' * width)


# nested group
def print_square(size):

  # For each row in a square, usally replace 'row' with 'i'
  for row in range(size):

    # For each brick inside of a row, usally replace 'inside_row' with 'k'
    for inside_row in range(size):
      print('#', end='')

    # print new line after every row not every brick(#)
    print()



# without the second loop
def print_square2(size):
  for i in range(size):
    print('#' * 3)



# or use a function to print row
def print_square3(size):
  for i in range(size):
    print_row(size)



main()
