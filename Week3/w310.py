#How to remove directories in Python

import os
os.chdir("/Users/maziar/py/COMP2155/Week3/testDir")
os.remove("/Users/maziar/py/COMP2155/Week3/testDir/basedOnW39.txt")
os.chdir("/Users/maziar/py/COMP2155/Week3/")
os.rmdir("/Users/maziar/py/COMP2155/Week3/testDir")

#r"C:\new" \n =>
# c: 
# ew