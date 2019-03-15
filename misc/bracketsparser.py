import argparse
import os

#Parameters to pass into this script
parser = argparse.ArgumentParser(description="Parenthesis/brackets checker")
parser.add_argument('--string', '-s', action='store', dest='string', help="Phrase to parse and check", required=True)
args = parser.parse_args()

tracker = []
for character in args.string:
	if character == "(" or character == "[" or character =="{":
		tracker.append(character)
	elif character == ")":
		if len(tracker) == 0:
			print("Invalid")
			exit(1)
		if tracker.pop() != "(":
			print("Invalid!")
	elif character == "]":
		if len(tracker) == 0:
			print("Invalid")
			exit(1)		
		if tracker.pop() != "[":
			print("Invalid!")
			exit(1)
	elif character == "}":
		if len(tracker) == 0:
			print("Invalid")
			exit(1)		
		if tracker.pop() != "{":
			print("Invalid!")
			exit(1)

if len(tracker) != 0:
	print("Invalid!")
	exit(1)

print("Valid!")