arr = [1, 2, 3, 4, 5]

arr.reverse()
print  arr

persons = ["john", "test1", "test111", 'a', "bbb"]

persons.reverse()
print persons

# append to end list
persons.append("my list")
print persons

# remove the end if dont have index list
persons.pop()
print  persons

persons.pop(2)
print persons

# insert by index
persons.insert(5, "thanh")
print persons

new_persons = ["relax time", "warking with python"]

# ghep 2 list
persons.extend(new_persons)
print persons

# tim kiem 1 phan tu
persons.index('thanh')
print persons.index('thanh')

# remove 1 phan tu
print persons.remove("thanh")

# sap xep
persons.sort()
print persons

# thay doi cac phan tu trong list

my_skills = ["react", 'node', 'html', 'css']

my_skills[2:] = ['java', 'python']

print my_skills

my_skills[3] = 'aws'

print  my_skills

my_skills[-1] = 'hiii'
print  my_skills

# loop
nums = [1, 2, 3, 4, 5]
sum = 0
len(nums)
for num in nums:
    sum += num
print "sum: %s" %sum


if 1 in nums:
    print "Is Found"

def hafl(e):
    return e/2

print map(hafl, nums)

def soChan(e):
    return e % 2 == 0

print filter(soChan, nums)


