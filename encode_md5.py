##Introduction to the user
print "\n\nHello!";
print "\nThis is a simple md5sum encoder I wrote in Python.";
print "\nYou can find this on http://github.com/paradoxdjell/hashcracker"

##Take input from the user
inp = raw_input("\nEnter the word whose md5sum is to be found: ")
print "\nYou entered", inp

##import hashlib library to check for hash
import hashlib

##Core hashing algorithm
s = hashlib.md5(inp.encode())

##Output of the hash
print "\nThe md5sum is", s.hexdigest()

##Bye bye
