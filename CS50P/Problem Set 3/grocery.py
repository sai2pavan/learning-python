dict1 = {}
while True:
    try:
        item = input().lower().strip()
        if item in dict1:
            dict1[item] += 1
        else:
            dict1[item] = 1
    except EOFError:
        break
dict1 = dict(sorted(dict1.items()))
for i in dict1:
    print(dict1[i],i.upper())