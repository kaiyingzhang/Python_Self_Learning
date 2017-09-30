# - *- coding: utf- 8 - *-

my_name = 'Kein'
my_age = 22
my_height = 167 #cm
my_weight = round(124.3333) #lbs
my_eye = 'black'
my_teeth = 'white'
my_hair = 'black'

print "let's talk about %s."% my_name
print "She's %d cm tall."% my_height
print "She is %d pound weight." % my_weight
print "She's got %s eyes and %s hair."%(my_eye,my_hair)

hilarious = False
joke_evaluation = "isn't that joke so funny?! %r"

print joke_evaluation % hilarious # result : isn't that joke so funny

print "." * 10

end1 = "C"
end2 = "H"
end3 = "I"
end4 = "N"
end5 = "A"

print end1 + end2 + end3,
print end4 + end5 

print "its fleece was white as %s." % 'snow' #its fleece was white as snow.

print "its fleece was white as %s." % "snow" #its fleece was white as snow.

print "its fleece was white as %r." % 'snow' #its fleece was white as 'snow'.

print end1 + end2 + end3+end1 + end2 + end3+end1 + end2 + end3+end1 + end2 + end3+end1 + end2 + end3
print end4 + end5 

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)

formatter1 = "%s %s %s %s"
 
print formatter1 % ("哈哈哈、", 2, 3, 4)
print "hello chinese %s" % '哈哈哈'
print "hello chinese %s" % '哈哈哈'

days = " Mon Tue Wed Thu Fri Sat Sun"
months = " Jan\nFeb\nMarch\nApril\nMay\nJune\nJuly"

print "Here are the days :", days
print "Here are the months : ", months

print """
there's something going on here
with the three double-quotes
we'll be able to type as much as we like
"""
 

print " im \\ a \\ cat"

print " \t Cat\n\t* grass"

print "im a split \non a line"

 
#while True:
 #  for i in [ "/","-","|","\\","|"]:
  #   print "%s\r" % i



