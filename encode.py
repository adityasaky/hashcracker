print "Hello";
print "\nThis is a simple md5 encoder.";
print "\nYou can find this on http://github.com/paradoxdjell/hashcracker"

inp = raw_input("word: ")
print "You entered ", inp

import hashlib
m = hashlib.md5()

m.update(inp)
print m.hexdigest()
