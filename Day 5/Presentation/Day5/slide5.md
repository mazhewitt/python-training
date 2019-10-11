# **while** (hoovering == true) i_am_busy
- The **while** statement looks similar to an if statement. Initially starts with condition check. At the end of an if clause, the program execution continues after the if statement. But at the end of a while clause, the program execution **loops** back to the start of the while statement: 
```
rooms_to_hoover = 5
hoover_works = True
while (hoover_works == True) and (rooms_to_hoover > 0):
    print('i am busy')
```
- Endless(infinite) while loop fix
```
rooms_to_hoover = 5
hoover_works = True
while (hoover_works == True) and (rooms_to_hoover > 0):
    print('i am busy')
    rooms_to_hoover = rooms_to_hoover - 1
```
- How many times "I am busy" will be printed?
- Python syntax: **while** keyword, condition, colon, indented block of code starting from next line.