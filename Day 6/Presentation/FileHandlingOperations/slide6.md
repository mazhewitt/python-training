# Read Information from File
- The `open()` function returns a file object, which has a `read()` method for reading the content of the file
- Typically reading is done within the body of a loop
- Each execution of the loop will read a line from the file into a string
- Format:
    ```
    for <variable to store a string> in <name of file variable>:
        <Do something with the string read from file>
    ```
- Example:
    ```
    f = open("test.txt")
    # print only the first line of file
    print(f.readline())
    ```
    ```
    f = open("test.txt") 
    # print all lines
    for line in inputFile:
    	print(line)
    ```
