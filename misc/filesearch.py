import os
import argparse

#Parameters to pass into this script
parser = argparse.ArgumentParser(description="Inputs needed to run the file searching Python program")
parser.add_argument('--file', '-f', action='store', dest='file', help="File name to find", required=True)
parser.add_argument('--dir', '-d', action='store', dest='dir', help='Directory to search', required=True)

args = parser.parse_args()

print("Welcome to Terry's File Search Python Program!")

founded_files = []

for root, dirs, files in os.walk(args.dir):
  for file in files:
  	if file == args.file:
  		founded_files.append(os.path.join(root, file))

if len(founded_files) >= 1:
	print(founded_files)
	exit()

  		

print("No file(s) %s was found" % args.file)

