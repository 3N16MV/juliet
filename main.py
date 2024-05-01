#
# Alexis '3N1GMV' Lariviere
# CYB333-25957 Ch. 8 Ex. 4
# 13APR2024
# 'Juliet' Unique Word Alphabetizer
# Written in Python 3.11 using PyCharm
#

#specify the python interpreter to use
#!/usr/bin/env python3

# Open text file in read mode and close the file
file_path = "romeo.txt"
file = open(file_path, 'r')
lines = file.read()
content = file.read()
JulietList = []

#Split the words in the file using the split() function
words = lines.split()

# Create a list of uniq1ue words and sort alphabetically
for word in words:
    if word in JulietList:
        continue
    JulietList.append(word.lower())
print(sorted(JulietList))

# Print Done and prompt user to exit the program
print("Done.")
print("Press Enter to exit.")
input()
exit()