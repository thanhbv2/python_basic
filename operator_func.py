print "10 > 3: %s " % (10 > 3)

print "5 >= 5: %s" % (5 >= 5)

z = 10
print " 1 < z < 20: %s " % (1 < z < 20)

isTrue = True
isFalse = False

print isTrue and isTrue

print isTrue and isFalse

print isFalse and isTrue

print isFalse and isFalse

print isTrue or isFalse

print isTrue or isTrue

print isFalse or isTrue

print isFalse or isFalse

name = "Bui van thanh"

# Membership Operators

print "thanh" in name

print 1 in [1, 4, 10, 12]

print 2 in [0, 1, 4]

print 2 not in [0, 1]

print 1 not in [1]

# Indentity Operators
first_name = name
print first_name is name
print first_name is not name