temp = ''
res = ''

for letter in s:
    if len(temp) == 0:
        temp = letter
        continue
        
    if letter >= temp[len(temp) - 1]:
        temp += letter
    else:
        if len(temp) > len(res):
            res = temp
            temp = letter
        else:
            temp = letter

if len(temp) > len(res):
    res = temp
print('Longest substring in alphabetical order is:', res)