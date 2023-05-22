str = input()
lst = ""
for i in str:
    if ord(i) < 97:
        var = ord(i) + 32
    else:
        var = ord(i) - 32
    lst += chr(var)
print(lst)