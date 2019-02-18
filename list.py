colors = ["react", "node", "test"]

# Luu tren cung 1 vung nho
b = colors

b.append("thuy tun")
print(b)
print(colors)

lists = [1, 2, 3, 33, 23, 321, 321, 324, 1, 31, 13]
# [0:8:2]
# begin: 0
# end: 8
# offset: 2

new_list = lists[0:4]

# slice and offset
slice_offset = lists[0:5:3]

# copy
lists_copy = lists[:]

# reverse list
reverse_list = lists[::-1]

print new_list
print slice_offset
print lists_copy
print reverse_list
print lists

