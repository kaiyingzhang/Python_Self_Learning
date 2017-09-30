from sys import argv
from os.path import exists

script,from_file,to_file = argv

print " copying from %s to %s..." % (from_file,to_file)

in_file = open(from_file)
indata = in_file.read()


print "Does the file exists? %r"% exists(to_file)

print "hit 'return' to continue..."
raw_input('>')


target = open(to_file,'w')
target.write(indata)

target.close()

print "target had been input..."

#!!!
in_file.close()

print "let's do it in one line..."

target = open(from_file,'w')
target.write("this is a new file and i rewrite it now!")
target.close()

open(to_file, 'w').write(open(from_file).read()) #success!





