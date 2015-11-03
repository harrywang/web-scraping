import re
oldfile = open('university.txt', 'rb')
newfile = open('newuniversity.txt', 'w')
#file = open('output', 'r')
for line in oldfile:
	universityname = line.strip("0123456789-.\t\n ")

	# m = re.search(r'\d+$', line)
	# if the string ends in digits m will be a Match object, or None otherwise.
	# if m is not None:
		# print m.group()
	if len(universityname)!=0:
		newfile.write("{ value: \"" + universityname + "\", data: \"" + universityname + "\" },\n")

oldfile.close()
newfile.close()


