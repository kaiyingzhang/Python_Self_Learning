#ex30 else if


people = 20
cats = 30
dogs = 15

if people < cats :
 print " too many cats!"
 
dogs += 5

if dogs == people:
 print "yeah!"
 
if dogs > cats:
 print "hello"
elif dogs < cats:
 print "elif is ok!"
else:
 print "else if ok"
 
if cats < dogs:
 print "hello"
elif dogs == cats:
 print "elif is ok!"
else:
 print "else if ok"
 
 
print dogs,"!",cats
