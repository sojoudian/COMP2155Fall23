#Print Wordking directory (folder)
import os
os.mkdir("testDir")
os.chdir("testDir")
#pwd
current_dir = os.getcwd()
print(current_dir)

a= "created using w39"
file_one = open("basedOnW39.txt", "w+")
file_one.write(a)
file_one.close

