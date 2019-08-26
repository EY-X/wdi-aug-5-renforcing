number_list = {}
for x in range(1, 51):
    if x % 2 == 0 and x % 7 == 0:
        number_list[x] = x*2
    elif x % 2 == 0:
        number_list[x] = x + 1
    elif x % 7 == 0:
        number_list[x] = x - 1
    else:
        number_list[x] = x

print(number_list)