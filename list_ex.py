list = [1, 2, 3, 4, 5]

print (2 ** 5)

def sum(items):
    tong = 0
    for i in items:
        tong += i

    return tong


print sum(list)


def multip(el):
    return el * 2


print map(multip, list)


def find_in_list(ds):
    max = ds[0]
    for el in ds:
        if el > max:
            max = el

    return max


print find_in_list(list)


