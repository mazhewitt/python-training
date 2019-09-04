# Indentation and Blocks
- Python uses whitespace and indents to denote blocks of code
- Lines of code that begin a block end in a colon:
- Lines within the code block are indented at the same level
- To end a code block, remove the indentation
- You'll want blocks of code that run only when certain conditions are met
- Example: (Python Devs be like, "Semi colons and curly braces are NOT needed!")
    - In Java:
    ```
    for(int i = 0; i < 10; i++) {
        System.out.println("Hello World 10 times");
    }
    System.out.println("After 10 times Hello World");
    ```
    - In Python: 
    ```
    for i in range(10):
    	print("Hello World 10 times")
    print("After 10 times Hello World")
    ```