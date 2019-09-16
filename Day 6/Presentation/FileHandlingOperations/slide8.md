# Write to a file
- How to do it:
    - Open the file and associate the file with a file variable (file is “locked” for writing).
    - A command to write the information.
    - A command to close the file.
- Use the `write()` function in conjunction with a file variable
- Format:
    - `outputFile.write(temp)`
- Example:
    ```
    # Assume that temp contains a string of characters.
    outputFile.write (temp)
    ```