fileName=input("Enter name of the file: ")
CURRENT_FILE=open(fileName, "r")

a=CURRENT_FILE.read()
# for line in a:
#     print(line)

print(a)

CURRENT_FILE.close()