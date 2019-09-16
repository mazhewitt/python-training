# Write to an Existing File
- To write to an existing file, you must add a parameter to the `open()` function:
- "a" - Append - will append to the end of the file
- "w" - Write - will overwrite any existing content
    - Example
    - Open the file "demofile2.txt" and append content to the file:
    ```
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()
    #open and read the file after the appending:
    f = open("demofile2.txt", "r")
    print(f.read())
    ```
    - Example
    - Open the file "demofile3.txt" and overwrite the content:
    ```
    f = open("demofile3.txt", "w")
    f.write("Woops! I have deleted the content!")
    f.close()
    #open and read the file after the appending:
    f = open("demofile3.txt", "r")
    print(f.read())
    ```