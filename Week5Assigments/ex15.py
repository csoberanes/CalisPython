#this imports the argument variable
from sys import argv

#this  unpacks argv and assigns it 2 variables
script, filename = argv

#This line assigns the file to a variable named txt
txt = open(filename)

#This line prints the filename
print "Here's your file %r:" % filename
#this line reads the content of the txt variable and prints it out
print txt.read()

#prompt user to type filename again and stores it as a variable
print "Type the filename again:"
file_again = raw_input("> ")

#opens file_again file and assigns it to the variable txt_again
txt_again = open(file_again)

#reads and prints txt_again variable
print txt_again.read()