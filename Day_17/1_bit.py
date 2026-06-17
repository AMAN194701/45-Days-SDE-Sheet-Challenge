arr = [2, 3]

n = len(arr)
ans = []

for mask in range(1 << n):

    total = 0

    for i in range(n):

        if mask & (1 << i):
            total += arr[i]

    ans.append(total)

print(ans)