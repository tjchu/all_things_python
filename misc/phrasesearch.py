import argparse
import os

#Parameters to pass into this script
parser = argparse.ArgumentParser(description="Inputs needed to run the phrase searching Python program")
parser.add_argument('--phrase', '-p', action='store', dest='phrase', help="Phrase to find", required=True)
parser.add_argument('--dir', '-d', action='store', dest='dir', help='Directory to search', required=True)
args = parser.parse_args()

print("Welcome to Terry's Phrase Search Program")
print("This program will be able to recursively find a phrase in a file or a directory") 


# os.walk() can traverse through all of the subdirectories and list all of the files and directories
# in each directory it traverses through. 
# It returns a tuple (current_directory, sub-directories in the current dir, files in current dir)
for _, _, files in os.walk(args.dir):
	for file in files:
		with open(file) as f:

			# Use enumerate() - adds counter to an iterable and returns it. 
			# The returned object is a enumerate object.
			for linenumber, line in enumerate(f, 1):
				if args.phrase in line:
					print("The '%s' is in file '%s' on line %d" % (args.phrase, file, linenumber))
		

print("Phrase searching done.")


#This can be done in Shell command grep in ONE LINE!
# grep -rnw '/path/to/somewhere/' -e 'pattern'

