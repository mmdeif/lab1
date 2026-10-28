   # AЛГОРИТМ1
def pointers(m,n):
    i=0
    j=0
    while (i< (len(m))) and (j< (len(n))):
        if m[i]<n[j]:
            i+=1
        elif m[i]>n[j]:
            j+=1
        else:
            return True
    return False

   # АЛГОРИТМ2
def bin_s(a,b):
    if len(a) > len(b):
        a, b = b, a
    for x in a:
        l=0
        r=len(b)-1
        while l<=r:
            m = (l + r) // 2
            if b[m]<x:
                l=m+1
            elif b[m]>x:
                r=m-1
            else:
                return True
    return False


    # АЛГОРИТМ3
def point_2(m, n):
    if len(m) < 1 or len(n) < 1:
        return False

    if len(m) > len(n):
        m, n = n, m

    i = 0
    start = 0

    while i < len(m) and start < len(n):
        x = m[i]

        if n[start] == x:
            return True
        if n[start] > x:
            i += 1
            continue

        step = 1
        j = start + step
        while j < len(n) and n[j] < x:
            step *= 2
            j = start + step

        if j >= len(n):
            j = len(n) - 1

        l = start + 1
        r = j
        while l <= r:
            mid = (l + r) // 2
            if n[mid] < x:
                l = mid + 1
            elif n[mid] > x:
                r = mid - 1
            else:
                return True

        start = l
        i += 1

    return False

    # АЛГОРИТМ4
def bin_c(b,l,r,x):
    while l <= r:
        m = (l + r) // 2
        if b[m] < x:
            l = m + 1
        elif b[m] > x:
            r = m - 1
        else:
            return True, l
    return False, l

def binar2(m, n):
    if len(m) > len(n):
        m, n = n, m

    def poisk(ml, mr, l, r):
        if ml > mr or l > r:
            return False
        mid = (ml + mr) // 2
        x = m[mid]
        found, l1 = bin_c(n, l, r, x)
        if found == True:
            return True
        if poisk(ml, mid - 1, l, l1 - 1):
            return True
        return poisk(mid + 1, mr, l1, r)

    return poisk(0, len(m) - 1, 0, len(n) - 1)