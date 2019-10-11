# File Close Operation
- `close()` method on a file will free up the resources that were tied with the file.
- Python has a garbage collector to clean up unreferenced objects.
- Format:
    - `<name of file variable>.close()`
- Example:
    - `inputFile.close()`
```
f = open("test.txt") 
# perform file operations
f.close()
```