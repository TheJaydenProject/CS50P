score1 = int((input('Score: ')))




# PSLE metric
# Assume numbers will always be between 1-100
if score1 >= 90:
  print('AL: 1')
elif score1 >= 85:
  print('AL: 2')
elif score1 >= 80:
  print('AL: 3')
elif score1 >= 75:
  print('AL: 4')
elif score1 >= 65:
  print('AL: 5')
elif score1 >= 45:
  print('AL: 6')
elif score1 >= 20:
  print('AL: 7')
else:
  print('AL: 8')


score2 = int((input('Score: ')))

# Being Precise because i want to catch errors numbers not between 1-100
if 90 <= score2 < 100:
  print('AL: 1')
elif 85 <= score2 < 90:
  print('AL: 2')
elif 80 <= score2 < 85:
  print('AL: 3')
elif 75 <= score2 < 80:
  print('AL: 4')
elif 65 <= score2 < 75:
  print('AL: 5')
elif 45 <= score2 < 65:
  print('AL: 6')
elif 20 <= score2 < 45:
  print('AL: 7')
elif 0 <= score2 < 20:
  print('AL: 8')
# Catch errors
else:
  print('Please enter valid numbers (1-100)')