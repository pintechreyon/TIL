num_product = 1
for n in range(3):
    num = int(input())
    num_product *= num

for i in range(10):
    result = 0
    for j in list(str(num_product)):
        if str(i)==j:
            result += 1
    print(result)