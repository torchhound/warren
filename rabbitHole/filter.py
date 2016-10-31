f = open("links.txt", "r")
f1 = open("cleanedLinks.txt", "w")

for line in f:
    if "javascript:void(0)" in line or "login?" in line or "vote?" in line or "item?" in line or "user?" in line or "hide?" in line or "fave?" in line or "reply?" in line:
        pass
    else:
        f1.write(line + "\n")
