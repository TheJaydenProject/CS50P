# Say hello world
print('Hello, world!')

# Ask user for their name
name = input('whats your name? ') # Input function expects a string

# Remove whitespace from str (only from left and right not in between)
name = name.strip()

# Capitalize User Name (first letter)
name = name.capitalize()

# Remove whitespace from str and Capitalize User name (every first letter of a new word)
name = name.strip().title()

# Can combine with the input if needed
name = input('whats your name? ').strip().title()

# Say hello to the user
print('Hello, ' + name)

# Another way to format strings
print('Hello,', name)

# Most Standard way
print(f'hello, {name}')

# Print Doc
# print(*objects, sep=' ', end='\n', file=None, flush=False)
# *objects: Any number of objects can be printed.
# sep: String inserted between values, default is a space.
# end: String appended after the last value, default is a newline (\n).
# file: An object with a write(string) method; defaults to the current sys.stdout.
# flush: A boolean, specifying whether to flush the output buffer.

# Solve Name being printed on a new line
print('Hello, ')
print(name)

# Solution
print('Hello,', sep=' ', end='')
print(name)

# Putting Quotes in quotes of Print function
# Use different quotes to seperate
print("Hello, 'friend'")
# Or use back slash
print('Hello, \'friend\'')


