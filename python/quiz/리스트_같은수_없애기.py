list_1 = input()

list_2 = []
for item in list_1:
    if item != '[':
        if item != ']':
            if item != ',':
                if item not in list_2:
                    list_2.append(item)
result = list(map(int,list_2))
print(result)
