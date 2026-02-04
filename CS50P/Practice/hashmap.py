arr = [10, 20, 30, 40]
freq = {}
duplicate = False

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for j in freq:
    if freq[j] > 1:
        duplicate = True

print(duplicate)