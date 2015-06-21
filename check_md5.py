print "\n\nHello!";
print "\nThis is a simple hashcracker I wrote in Python.";
print "\nYou can find this on http://github.com/paradoxdjell/hashcracker"
print "\nFeel free to use your own wordlist. Just replace words.txt with your own file and ensure it is named words.txt.";

import sys

inp = raw_input("\nEnter the md5sum: ")
print "\nYou entered", inp
if len(inp) != 32:
    print "This isn't an md5sum."
    sys.exit()

import hashlib

fh = open("words.txt", "r")

flag = 0;

for line in fh:
    s = hashlib.md5(line.rstrip().encode())
    if inp == s.hexdigest():
        print "\nMatch found -", line
        flag = 1;
        break

if flag == 0:
    print "\nNo match found. Try a different wordlist?"

fh.close();
