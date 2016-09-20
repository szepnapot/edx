s = 'azcbobobegghakl'

total = 0

for i in range(len(s)):
    if s[i] == 'b' and s[i:i+3] == 'bob':
        total += 1

print(total)