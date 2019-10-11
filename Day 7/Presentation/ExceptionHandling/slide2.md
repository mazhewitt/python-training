# Exception Handling
- When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
- These exceptions can be handled using the try statement:
    - Example
    - The try block will generate an exception, because x is not defined:
    ```
    try:
        print(x)
    except:
        print("An exception occurred")
    ```
- Since the try block raises an error, the except block will be executed.
- Without the try block, the program will crash and raise an error:
    - Example
    - This statement will raise an error, because x is not defined:
    ```
    print(x)
    ```

