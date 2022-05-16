

def F(n):
    if n == 0:
        return 0
    if n % 3 != 0:
        return F(n - 1) + 1
    if n > 0 and n % 3 == 0:
        return F(n // 3)

ans = set()
max_k = 0
for n in range(1200000000, 1600000000 + 1):
    try:
        ans.add(F(n))
    except:
        pass
print(max(ans))
