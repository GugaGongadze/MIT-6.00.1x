counter = 0;
for i in range(len(s) - 2):
  if s[i] + s[i + 1] + s[i + 2] == 'bob':
    counter += 1;
print('Number of times bob occurs is: ' + str(counter));