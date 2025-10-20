# list
students = ['Hermione', 'Harry', 'Ron']

# print everything in list
for student in students:
  print(student)

# Another way
# range only take int() so len() returns the number of items in list
# index/i is the loop variable - it takes on each value from the range (0, 1, 2...) as the loop runs
for index in range(len(students)):
  print(index + 1, students[index])