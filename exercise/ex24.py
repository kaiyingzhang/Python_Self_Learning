#exercise 24

print "let's practise something"
print "You \'d need to know \'about escape with \\ that do \n newlines and \t tabs"

poem = """
\t the lovely world 
with logic so firmly planted
cannot discern \n the needs of lovelynor comprhend passion form intuition
and requies an explanation
\t\n\t where there is none.
"""

print "---------"

print poem

print "---------"

def secret_formula(started):
 jelly_beans = started * 500
 jars = jelly_beans /1000
 crates = jars /100
 return jelly_beans,jars,crates

start_point = 10000

beans,jars,crates = secret_formula(start_point)

print "with a starting point of : %d" %start_point
print "we'd have %s beans, %s jars, %s crates"% (beans, jars, crates)

print "we can also do that this way : "
print "we'd have %d beans, %d jars, %d crates"% secret_formula(100000)