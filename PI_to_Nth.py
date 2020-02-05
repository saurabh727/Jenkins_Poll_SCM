pi = str(22/7)
pi_split = pi.split('.')
pi_split_left = pi_split[0]+'.'
pi_split_right = list(pi_split[1])
limit = int((input('Enter the limit')))
print(limit)
range1 = pi_split_right[0:limit]
for i in range1:
    pi_split_left = pi_split_left+i

print(pi_split_left)
