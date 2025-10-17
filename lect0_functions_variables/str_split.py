# Split user input (one str) to multiple strs
name = input('What\'s your name? ').strip().title().split()

# Eg user give first and last name, output only first name
first_name = name[0]
last_name = name[1]

print(f'Hello, {first_name}')


# A cleaner way to do it
name = input('What\'s your name? ').strip().title()

first_name, last_name = name.split(' ')
print(f'Hello, {first_name}')