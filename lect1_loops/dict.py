# dictionary
students = {
  # Key - # Value
  'Hermione': 'Gryffindor',
  'Harry': 'Gryffindor',
  'Ron': 'Gryffindor',
  'Draco': 'Slytherin'
}

print(students['Harry'])
print(students['Draco'])

# Loop through each student name (key) in the dictionary
for student in students:
  print(student, students[student], sep = ", ")