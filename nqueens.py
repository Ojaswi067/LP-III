def safe(b, r, c, n):
    for i in range(r):
        if b[i][c] == 1 or \
           (c-r+i >= 0 and b[i][c-r+i] == 1) or \
           (c+r-i < n and b[i][c+r-i] == 1):
            return False
    return True


def solve(b, r, n):
    if r == n:
        for row in b:
            print(row)
        print()
        return

    for c in range(n):
        if safe(b, r, c, n):
            b[r][c] = 1
            solve(b, r+1, n)
            b[r][c] = 0


n = int(input("n: "))
print("N queens for n =", n)

b = [[0]*n for _ in range(n)]
solve(b, 0, n)