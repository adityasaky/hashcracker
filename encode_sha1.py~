print "\n\nHello!";
print "\nThis is a simple md5sum encoder I wrote in Python.";
print "\nYou can find this on http://github.com/paradoxdjell/hashcracker"

inp = raw_input("\nEnter the word whose md5sum is to be found: ")
print "\nYou entered", inp

import hashlib

s = hashlib.md5(inp.encode())
print "\nThe md5sum is", s.hexdigest(),"."
