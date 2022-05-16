with open('17.txt') as file:
    s = [int(i) for i in file.readlines()]

k = 0
sr = 0
for i in s:
    if i % 2 != 0:
        sr += i
        k += 1
sr /= k
m = 0
max_s = 0
for i in range(len(s) - 2):
    if s[i] % 3 != s[i + 1] % 3 and s[i] % 3 != s[i + 2] % 3 and s[i + 1] % 3 != s[i + 2] % 3:
        if (s[i] < sr and s[i + 1] >= sr and s[i + 2] >= sr) or \
            (s[i + 1] < sr and s[i] >= sr and s[i + 2] >= sr) or \
            (s[i + 2] < sr and s[i + 1] >= sr and s[i] >= sr):
            m += 1
            max_s = max(max_s, s[i] + s[i + 1]+ s[i + 2])
print(m, max_s)
