import re
oldfile = open('country.txt', 'rb')
newfile = open('newcountry.txt', 'w')
#file = open('output', 'r')
for line in oldfile:
	line = line.strip()
	if line.startswith("<option"):
		index1 = line.index(">");
		index2 = line.index("</option")
		countryname = line[index1+1:index2]  # country name

		index3 = line.index("spellings=");
		shortname = line[index3+11:index3+13]  # country alternative spellings

		newline = "{ value: \"" + countryname + "\", data: \"" + shortname + "\" },\n"
		newfile.write(newline)

oldfile.close()
newfile.close()


