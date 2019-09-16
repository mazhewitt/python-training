# Read Lines
- You can return one line by using the `readline()` method:
    - Example
    - Read one line of the file:
    ```
    f = open("demofile.txt", "r")
    print(f.readline())
    ```
- By calling readline() two times, you can read the two first lines:
    - Example
    - Read two lines of the file:
    ```
    f = open("demofile.txt", "r")
    print(f.readline())
    print(f.readline())
    ```