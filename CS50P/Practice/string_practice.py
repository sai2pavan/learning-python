s1 = "listen"
s2 = "swastik"

anagram = True

dict1 = {}
dict2 = {}

if len(s1) != len(s2):
    anagram = False
else:
    for i in s1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    for j in s2:
        if j in dict2:
            dict2[j] += 1
        else:
            dict2[j] = 1

    for k in dict1:
        if dict1[k] != dict2.get(k, 0):
            anagram = False
            break

print(anagram)