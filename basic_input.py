#!python
""" playing with some basic input and output """
import sys

# Unique ones including the script name
# arguments = set(sys.argv)
# print "Passed in {} arguments, with {} unique ones, they are :".format(len(sys.argv), len(arguments))

# Unique arguments not including the script name
arguments = set()
print "Passed in {} arguments, they are :".format(len(sys.argv) - 1)
for arg in xrange(1, len(sys.argv)):
     arguments.add(sys.argv[arg])

print arguments
