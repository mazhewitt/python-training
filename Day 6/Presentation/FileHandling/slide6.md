# Read Lines
- By looping through the lines of the file, you can read the whole file, line by line:
    - Example
    - Loop through the file line by line:
    ```
    f = open("demofile.txt", "r")
    for x in f:
        print(x)
    ```