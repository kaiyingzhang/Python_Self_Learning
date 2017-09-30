from sys import argv

script, user_name = argv
prompt = '>'

print "Hi, %s, im the %s script"%(user_name,script)
print "do you like me, %s?" % user_name
like = raw_input(prompt)
#prompt means the terminal will show the things you defined for prompt and than u can input the things.

print "hahaha= %s"% like  
#%s will show the content you input but %r will show the character with ''

print """
hahah 
this is an attempt
hahaha
how
"""