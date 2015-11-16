# file operations
file=open("test.txt",'a')
file.write("Some content \n")
file.close

# Read the file contents
file=open("test.txt",'r')
contents=file.read()
print("Contents of test.txt are:"+contents)