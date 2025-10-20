
# good habit to start from 0
i = 0

# loops through 3 times using while loop
while i < 3:
  print('Meow')
  i += 1

# use for loop with range
# use _ to show that _ has no meaning (just placeholder)
for _ in range(3):
  print('meow')

# Not the best way but still a way
print('mew\n' * 3, end='')

# loop through till valid input (positive integer)
while True:
  n = int(input('What\'s n? '))
  if n > 0:
    break

for _ in range(n):
  print('Meowwww')
