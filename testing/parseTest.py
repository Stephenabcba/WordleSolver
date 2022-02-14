from os import sep


fo = open("test.txt","r")
output = open("out.txt","w+")
curLine = fo.read()
seperated = curLine.split(";")
print(len(curLine))
print(len(seperated))
for line in seperated:
    output.write(line)
    output.write(";\n")