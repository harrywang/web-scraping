f1 = open('usa_univ_names.txt', 'r')
x = f1.readlines()
f2 = open('world_univ_names.txt', 'r')
y = f2.readlines()
x.extend(y)
z = []
for line in x:
    z.append(line.strip())

z.sort()
with open('all_univ_names.txt', 'w') as f:
    for s in z:
        f.write(s + '\n')
