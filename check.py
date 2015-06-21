print "Hello";
print "\nThis is a simple Hash cracker based on the Cain wordlist.";
print "\nYou can find this on http://github.com/paradoxdjell/hashcracker"

inp = raw_input("Enter the md5 sum: ")
print "You entered ", inp

class A:
    def assignment(self):
        line = fh.readline()

a = A()

import hashlib
m = hashlib.md5()

fh = open("words.txt", "r")

flag = 0;

for line in fh:
    a.assignment
    m.update(line)
    s = m.hexdigest()
    if inp == s:
        print "Match found! - ", line
        flag = 1;
        break

if flag == 0:
    print "No match found."

fh.close();
