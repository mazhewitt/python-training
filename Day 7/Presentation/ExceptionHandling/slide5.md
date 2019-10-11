# Python Try Except
- The finally block, if specified, will be executed regardless if the try block raises an error or not.
    - Example
    ```
    try: 
        print(x)
    except:
        print("Something went wrong")
    finally:
        print("The 'try except' is finished")
    ```
- This can be useful to close objects and clean up resources:
    - Try to open and write to a file that is not writable:
    ```
    try:
        f = open("demofile.txt")
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
    ```
    - The program can continue, without leaving the file object open.

