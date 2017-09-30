#ex20 functions and files

from sys import argv

script, input_file = argv

def print_all(file):
 print file.read()
 
def rewind(f):
 f.seek(0)
 
def print_a_line(f):# readline can remember the position every time after it read the content
 f.readline()
 
print "let's print the whole file : %r" % input_file

def print_file(f):
 f_content=open(f)
 print "content: ", f_content.read()
 
print_file(input_file)

print "let's rewind the file : %r " % input_file

#rewind(open(input_file))
print "let's print a line :"
print_file(input_file)
