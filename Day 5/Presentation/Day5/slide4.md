# Chaining Conditions: **if** moustache == true Grandpa **else** Grandma
- Alternative execution offers two paths to follow based on the condition test result:
```
name = 'Hamlet'
skulls_number = 1
if (name == 'Hamlet') and (skulls_number > 1):
    print('To be or not to be')
else:
    print('Neither here nor there')
```
- Chained conditions: elif
```
name = 'Hamlet'
skulls_number = 1
if (name == 'Hamlet') and (skulls_number > 1):
    print('To be or not to be')
elif skull_number == 1:
    print('The way madness lies')
else:
    print('Neither here nor there')
```
- Python syntax: elif keyword, condition, colon, indented block of code starting from next line.

