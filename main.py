lst = [10,30,40,60,12]
# lst.sort()
# print(lst[-2])

# max_val = max(lst)
# lst.remove(max_val)
# second_max = max(lst)
# print(second_max)

lar = lst[0]
slar = lar
for i in range(1,len(lst)):
    if lst[i] > lar:
        slar = lar
        lar = lst[i]
    elif lst[i]==lar:
        pass
    else:
        if lst[i] > slar:
            slar = lst[i]

print(lar, slar)
