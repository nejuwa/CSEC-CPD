from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = defaultdict(int)
l = 0
ll = 0
rr = 0
distinct = 0

for r in range(n):
    freq[a[r]] += 1
    if freq[a[r]] == 1:
        distinct += 1

    while distinct > k:
        freq[a[l]] -= 1
        if freq[a[l]] == 0:
            distinct -= 1
        l += 1

    if r - l > rr - ll:
        ll, rr = l, r

print(ll + 1, rr + 1)
