print("Ready!")

a= open("file.txt", "r", )
b= a.mode
c=a.name
print("Access of the file is: " + b + "\n" + "Name of the file is: " + c)

a.close
