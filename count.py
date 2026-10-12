s = "abcafghwrw"
seen = ""
for w in s:
    if w not in seen:
        seen = seen + w
print(len(seen))
