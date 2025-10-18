x = input('What\'s x? ')
y = input('What\'s y? ')

z = int(x) + int(y)

print(z)

# nest functions
x = int(input('What\'s x? '))
y = int(input('What\'s y? '))

print(x + y)

# floats
x = float(input('What\'s x? '))
y = float(input('What\'s y? '))

z = round(x + y)

# every 3 zeros add comma
print(f'{z:,}')

# division of floats
x = float(input('What\'s x? '))
y = float(input('What\'s y? '))

# outputing 2 decimals max but can have one less decimals (e.g. 1.00 = 1.0)
z = round(x / y, 2)

# every 3 zeros add comma
print(z)

# another way of outputing 2 decimals but ALWAYS 2 decimals
print(f'{z:.2f}')