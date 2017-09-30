# ex21 functions can return something

def add(a,b):
 print "adding %d and %d :" %(a,b)
 print int(a+b)
 
add(2,3)

print "please input two number you want to add :"
a=float(raw_input('a:'))
b=float(raw_input('b:'))

print "result of %d + %d :" % (a,b)
add(a,b)