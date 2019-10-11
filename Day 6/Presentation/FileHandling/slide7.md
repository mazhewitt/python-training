# Close Files
- It is a good practice to always close the file when you are done with it.
    - Example
    - Close the file when you are finish with it:
    ```
    f = open("demofile.txt", "r")
    print(f.readline())
    f.close()
    ```