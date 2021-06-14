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
    return c, sorted(range(n), key=lambda x: c[x])

def LCP(s):
    c, sa = SuffixArray(s)
    a = [0] * len(s)
    for i in range(len(s)):
        current, previous = i, sa[c[i] - 1]
        j = 0 if i == 0 else max(0, a[c[i-1] - 1] - 1)
        while 1:
            if max(current + j, previous + j) >= len(s): break
            if s[current + j] != s[previous + j]:
                break
            j += 1
        a[c[i] - 1] = j
    return a, sa
