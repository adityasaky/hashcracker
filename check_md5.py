##Introduction to the user
print "\n\nHello!";
print "\nThis is a simple hashcracker I wrote in Python.";
print "\nYou can find this on http://github.com/paradoxdjell/hashcracker"
print "\nFeel free to use your own wordlist. Just replace words.txt with your own file and ensure it is named words.txt.";

##import sys to allow exit, in case the input isn't appropriate
import sys

##Take input and check if appropriate
inp = raw_input("\nEnter the md5sum: ")
print "\nYou entered", inp
if len(inp) != 32:
    print "This isn't an md5sum."
    sys.exit()

##import hashlib library to check for hash
import hashlib

##Open the wordlist
fh = open("words.txt", "r")

##Set checking variable to false
flag = 0;

##Core checking algorithm
for line in fh:
    s = hashlib.md5(line.rstrip().encode())
    if inp == s.hexdigest():
        print "\nMatch found -", line
        flag = 1;
        break

##Check checking variable
if flag == 0:
    print "\nNo match found. Try a different wordlist?"

##Close the wordlist
fh.close();

##Bye bye
