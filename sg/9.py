with open('9.txt') as file:
    s = [[int(j) for j in i.split()] for i in file.readlines()]

# s = [[12, 13, 11, 14], [8, 6, 4, 10], [14, 1, 6, 8]]

k = 0
for i in s:
    f = False
    if i[0] + i[1] == i[2] + i[3]:
        if (i[0] + i[1]) % 2 != 0:
            f = True
    elif i[0] + i[2] == i[1] + i[3]:
        if (i[0] + i[2]) % 2 != 0:
            f = True
    elif i[0] + i[3] == i[1] + i[2]:
        if (i[0] + i[3]) % 2 != 0:
            f = True
    if f:
        k += 1
print(k)
