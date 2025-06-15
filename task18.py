#file handling
# mode 'r'
file=open("demo.txt",mode='r')
read=file.read()
print(read)
file.close()

#mode 'a'
file = open("demo.txt",mode='a')
write=file.write("hello guys this is python task")
file.close()

#mode 'a+'
file=open("demo.txt",mode='a+')
file.write("Appended using a+ mode.\n")
file.seek(0) #Move cursor to beginning to read
read=file.read()
print(read)
file.close()

#mode 'r+'
file=open("demo.txt",mode='r+')
read=file.read()
file.write("\nAdded using r+ mode.")
print(read)
file.close()

# mode 'w'
file=file=open("demo.txt",mode='w')
file.write("hi guys welcome to python now using w so all the before elements gets truncated")
file.close()

#mode 'w+'
file=open("demo.txt",mode='w+')
file.write("this is written using w+ mode.\n")
file.close()
