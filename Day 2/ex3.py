# Numbers and arithmetic operators

x = 1  # integer
y = 2.0  # everything with decimal point is float
print(type(x))
print(type(y))

a = 25  # Unlike strings, numbers don't require special decoration
b = '25'  # If you enclose a number in quotes, you'll get a string
print(type(b))

c = int(b)  # To get back a number, use built-in functions int(), float()
d = float(b)

# You can use Python as calculator
print("How many sandwiches can I buy with 100zl?:", 100 // 6)
print("How much money will I have left then?", 100 % 6)
