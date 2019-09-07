#Converting types
- Python is a loosely-type language
    - Meaning, we do not need to define the data types of the variables which we use
    - Implicit Type Casting:
    - Similar data types can automatically fit into each other
    - Eg: Integer to Float or vice versa
```
    i_am_int = 10
    i_am_float = 10.1
    i_am_float = i_am_int #New value is 10
```
- Explicit Type Casting:
    - Not-so-similar data types require us to specifically mention the conversion
    - Eg: String to Integer
```
    i_am_string = "10"
    i_am_int = 20
    addition = i_am_int + i_am_string #Compilation Error
    addition = i_am_int + int(i_am_string) #Explicit Type-Casting
```