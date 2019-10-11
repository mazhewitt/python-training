# File Open Operation
- Python has built in function to open a file `open()`
- It returns a file object, also called a handle, as it is used to read or modify the file accordingly
- Format : `<file variable> = open(<file name>, <mode>)`
    ```
    # open file in current directory
    f = open("test.txt")
    # specifying full path
    f = open("C:/Python34/README.txt")
    ```