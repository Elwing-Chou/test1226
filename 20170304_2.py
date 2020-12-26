_ = input()
line = input()
ls = line.split(" ")
friends = [int(f) for f in ls]

count = 0
already = set()
for i in range(len(friends)):
    if not i in already:
        start = i
        while not start in already:
            already.add(start)
            start = friends[start]
        count = count + 1
print(count)
