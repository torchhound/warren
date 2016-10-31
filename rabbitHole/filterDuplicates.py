f = open("cleanedLinks.txt", "r")
f1 = open("dedupCLinks.txt", "w")

lst = []

for line in f:
    lst.append(line)

st = set(lst)
f1.writelines(st)
