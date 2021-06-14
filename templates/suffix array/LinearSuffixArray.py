def SuffixArray(s):
    n = len(s)
    mp = list(map(ord, s))
    T = max(mp) + 3
    buckets = [0] * T
    a = []
    for x in mp:
        a += [x]
        buckets[x + 1] += 1
    for i in range(1, T):
        buckets[i] += buckets[i - 1]
    # color[i] = is suffix from i less than suffix from i+1?
    color = [1] * n
    lms = []
    # is index an LMS index?
    flag = [False] * (n + 1)
    flag[-1] = True
    for i in range(n - 2, -1, -1):
        if a[i] < a[i + 1]:
            color[i] = 0
        elif a[i] == a[i + 1]:
            color[i] = color[i + 1]
        if color[i] and not color[i + 1]:
            lms += [i + 1]
            flag[i + 1] = True
    lms = lms[::-1]
    
    def induced_sort(lms):
        sa = [-1] * n
        sa += [n]
        omega = buckets[1:]
        for j in reversed(lms):
            omega[a[j]] -= 1
            sa[omega[a[j]]] = j
        alpha = buckets[:-1]
        for i in range(-1, n):
            j = sa[i] - 1
            if j >= 0 and color[j]:
                sa[alpha[a[j]]] = j
                alpha[a[j]] += 1
        sa.pop()
        omega = buckets[1:]
        for i in reversed(range(n)):
            j = sa[i] - 1
            if j >= 0 and not color[j]:
                omega[a[j]] -= 1
                sa[omega[a[j]]] = j
        return sa
    
    sa = induced_sort(lms)
    if len(lms) <= 1:
        return [n] + sa
    lms2 = [i for i in sa if flag[i]]
    last = -1
    j = 0
    for i in lms2:
        p, q = last, i
        while last >= 0 and a[p] == a[q]:
            p += 1
            q += 1
            if flag[p] or flag[q]:
                j -= flag[p] and flag[q]
                break
        j += 1
        last = i
        sa[i] = j
    sa2 = SuffixArray([chr(sa[i]) for i in lms])
    lms = [lms[sa2[i]] for i in range(1, len(sa2))]
    return [n] + induced_sort(lms)


def LCP(s):
    sa = SuffixArray(s)
    c = sorted(range(len(s) + 1), key=lambda i: sa[i])
    a = [0] * len(s)
    for i in range(len(s)):
        current, previous = i, sa[c[i] - 1]
        j = 0 if i == 0 else max(0, a[c[i - 1] - 1] - 1)
        while 1:
            if max(current + j, previous + j) >= len(s): break
            if s[current + j] != s[previous + j]:
                break
            j += 1
        a[c[i] - 1] = j
    return a, sa
