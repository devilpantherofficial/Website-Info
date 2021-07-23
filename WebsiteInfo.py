import os
import sys
import urllib2
bred="\033[1;31m"
print("\033[0;32m")
os.system("figlet Website Info ")
print("\033[0;31m" )
print("DEVIL PANTHER")
print("\033[0;33m" )
print("Tools name is 'Website Info'")
print("\033[0;33m")
url =raw_input("Enter website link: ")

url.rstrip ( )
header = urllib2.urlopen (url) .info( )
print(str(header))
num = input(bred+"Type 0 for exit : ")
if num == "0":
  exit()
