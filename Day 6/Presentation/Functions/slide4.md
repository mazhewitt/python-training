# Default Parameter Value
- The following example shows how to use a default parameter value.
- If we call the function without parameter, it uses the default value:
    - Example
    ```
    def my_function(country = "Norway"):
        print("I am from " + country)
    my_function("Sweden")
    my_function("India")
    my_function()
    my_function("Brazil")
    ```
