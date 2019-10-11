# Open a File on the Server
- Assume we have the following file, located in the same folder as Python:
- demofile.txt
- `Hello! Welcome to demofile.txt`  
  `This file is for testing purposes.`  
  `Good Luck!`  
- To open the file, use the built-in `open()` function.
- The `open()` function returns a file object, which has a `read()` method for reading the content of the file:
    - Example
    ```
    f = open("demofile.txt", "r")
    print(f.read())
    ```