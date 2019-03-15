import argparse
import os

# Got asked this question by Amazon for an internship interview and had NO idea how to do it... :P 
# Now that I look back, this question is extremely easy. Goes to show how much I have improved.
# I told myself I will never mess up again if I ever got asked this question again.

# Here is to more failures to conquer :) 

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