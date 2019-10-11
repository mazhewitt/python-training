# Home Assignment 3
- #Q1. Write a Python program to concatenate only the last three charachters of both strings and print the output.

```
string_1 = "London"
string_1 = "Tokyo"

#expectedoutput: donkyo
string_1 = "London"
string_2 = "Tokyo"
string_3 = string_1[-3:] + string_2[-3:]
print(string_3)

```

- #Q2. Write a python program to create a list with values apple,mango,banana,
blueberry,orange and then print only the first two values from the following List 

```
fruits = ["apple","mango","banana","blueberry","orange"]
print(fruits[:2])

```

- #Q3. Write a python program to remove the value "apple" and insert value 
"pineapple" at the same index in the above list. Print the list once modified

```
fruits.remove("apple")
fruits.insert(0,"pineapple")
print(fruits)
```
