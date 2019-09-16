# Passing a List as a Parameter
- You can send any data types of parameter to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
- E.g. if you send a List as a parameter, it will still be a List when it reaches the function:
    - Example
    ```
    def my_function(food):
        for x in food:
            print(x)
    fruits = ["apple", "banana", "cherry"]
    my_function(fruits)
    ```