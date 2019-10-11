# Reading From Files: Putting It All Together
```
inputFileName = input("Enter name of input file: ")
inputFile = open(inputFileName, "r")
print("Opening file", inputFileName, " for reading.")

for line in inputFile:
	print(line)


inputFile.close()
print("Completed reading of file", inputFileName)
```