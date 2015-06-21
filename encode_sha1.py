print "\n\nHello!";
print "\nThis is a simple md5sum encoder I wrote in Python.";
print "\nYou can find this on http://github.com/paradoxdjell/hashcracker"

inp = raw_input("\nEnter the word whose sha1 is to be found: ")
print "\nYou entered", inp

import hashlib

s = hashlib.sha1(inp.encode())
print "\nThe sha1 is", s.hexdigest(),"."
