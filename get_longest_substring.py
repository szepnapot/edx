s = 'abcbcd'
old = ''
current = ''
for char in s:
    if current == '':
        current += char
    elif current[-1] <= char:
        current += char
    elif current[-1] > char:
        if len(old) < len(current):
            old = current
            current = char
        else:
            current = char

if len(current) < len(old) or len(current) == len(old):
    print('Longest substring in alphabetical order is: ' + old)
else:
    print('Longest substring in alphabetical order is: ' + current)