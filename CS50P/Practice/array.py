arr = [2, 4, 6, 8]
average = sum(arr) / len(arr)
count = 0

for i in arr:
    if i > average:
        count += 1

print(count)