#this one is like your scripts with argv

#that *args is actually pointless, we can just do this:
def print_two_again(arg1,arg2):
      print "arg1: %r, arg2: %r" % (arg1,arg2)
      
	  
#this just take one argument
def print_one(arg1):
      print "arg1 : %r" % arg1
	  
#this one takes no arguments
def print_none():
      print "i got nothing"
	  
	  


print_two_again("test5","test6")
print_one("...")
print_none()

def print_two(*args):
 arg1, arg2 = args
 print "arg1 : %r, arg2 : %r "%(arg1, arg2)
 #pay attention to the front sign of every line
 # a function should be included in a '["
	
print_two("test1","test2")
#print_two('test3','test4')  
	  