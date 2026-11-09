n = int(input("Enter number of items: "))

items = []
for i in range(n):
    w = int(input("Enter weight: "))
    p = int(input("Enter profit: "))
    items.append((p/w, w, p))

W = int(input("Enter knapsack capacity: "))

items.sort(reverse=True)

total = 0

for r, w, p in items:
    if W >= w:
        total += p
        W -= w
    else:
        total += r * W
        break

print("Maximum profit:", total)
