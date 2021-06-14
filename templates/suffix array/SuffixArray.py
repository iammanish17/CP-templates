def SuffixArray(s):
    n = len(s) + 1
    a = sorted(range(n-1), key=lambda i:s[i])
    c = [0] * n
    p = [n - 1]
    cur = 0
    for i in range(n-1):
        cur += (i==0 or s[a[i-1]] != s[a[i]])
        c[a[i]] = cur
        p += [a[i]]
    k = 1
    while 1:
        buckets = [[] for _ in range(n)]
        for x in p:
            prev = (x - k) if (x - k) >= 0 else x - k + n
            buckets[c[prev]] += [(c[prev], c[x], prev)]
        values = []
        for x in buckets:
            values += x
        c = [0] * n
        cur = 0
        p = [n - 1]
        for i in range(1, n):
            cur += ((values[i - 1][0], values[i - 1][1]) != (values[i][0], values[i][1]))
            c[values[i][2]] = cur
            p += [values[i][2]]
        if cur == n - 1:
            break
        k *= 2
    return sorted(range(n), key=lambda x: c[x])
