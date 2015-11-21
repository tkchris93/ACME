import time

a = []
before = time.time()
for i in xrange(10000):
    a.insert(0,i)
after = time.time()
insert_time = after - before

b = []
before = time.time()
for i in xrange(10000):
    b = [i] + b
after = time.time()
concat_time = after - before

c = []
before = time.time()
for i in xrange(10000):
    c.append(i)
after = time.time()
append_time = after - before

d = []


print "Insert: " + str(insert_time)
print "Concat: " + str(concat_time)
print "Append: " + str(append_time)
