# Writing To A File: Putting It All Together
```
inputFileName = input("Enter the name of input file to read : ")
outputFileName = input("Enter the name of the output file to record : ")

inputFile = open(inputFileName, "r")
outputFile = open(outputFileName, "w")
   
print("Opening file", inputFileName, " for reading.")
print("Opening file", outputFileName, " for writing.")
```