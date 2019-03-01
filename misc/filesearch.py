import os
import argparse

#Parameters to pass into this script
parser = argparse.ArgumentParser(description="Inputs needed to run this shit")
parser.add_argument('--file', '-f', action='store', dest='file', help="File name to find", required=True)
parser.add_argument('--dir', '-d', action='store', dest='dir', help='Directory to search', required=True)

args = parser.parse_args()


for root, dirs, files in os.walk(args.dir):
  for file in files:
  	if file == args.file:
  		print("FOUND:", os.path.join(root, file))


