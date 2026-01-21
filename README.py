# Problem-978B---File-Name
n = int(input())
s = input().strip()
count = 0
_remove = 0
for i in s:
    if i == "x":
        count += 1
        if count >= 3:
            _remove += 1
    else:
        count = 0
print(_remove)
