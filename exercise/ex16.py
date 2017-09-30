from sys import argv

script, filename = argv

txt = open(filename)
print "let's read this file: %r"% filename
print "\n content:"
print txt.read()


print "we are going to erase %r."% filename
print "if u don't want , hit CTRL-C"

raw_input("?")

print "opening the file..."
target = open(filename, 'w')#open this file in 'write' mode

print "truncating the file. goodbye"
target.truncate()

print "now im going to ask u for three lines"

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "im going to write these to the file..."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.write("%s%s%s"%(line1,line2,line3))

print "and finally, we close it"
target.close()

print "let's read the file: %r" % filename
print "start... \n"
txt2 = open(filename)
print txt2.read()
print "--end--"
