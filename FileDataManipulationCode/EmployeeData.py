#import the csv module
import csv

#open the first csv file
firstFileObject = open("EmployeeDetails.csv")

#read the content of first csv file using csv.reader function
employeeDetails = csv.reader(firstFileObject)

#convert the data into List
employeeDetailsList = list(employeeDetails)[1:]
print("\n*********************EMPLOYEE DETAILS***************\n")	
print(employeeDetailsList)	
print("****************************************************\n\n")	
	
#open the second csv file
secondFileObject = open("EmployeeSalaries.csv")

#read the content of second csv file
employeeSalary = csv.reader(secondFileObject)
employeeSalaryList = list(employeeSalary)

#here we will sort the content of the second file using gpn
employeeSalaryList.sort()


print("\n*********************EMPLOYEE SALARIES***************\n")
print(employeeSalaryList)
print("****************************************************\n\n")	

#Here we will add the salary data to the original list
for i in range(0,4):
	employeeDetailsList[i].append(employeeSalaryList[i][1])


print("\n*********************EMPLOYEE DATA***************\n")
print(employeeDetailsList)
print("****************************************************\n\n")	

#we will create a new csv file and insert the merged data into the file
employee = open("EmployeeData.csv","w+")
employee.write("GPN,Name,DOB,Salary\n")
for data in employeeDetailsList:
	employee.write(data[0]+','+data[1]+','+data[2]+','+data[3]+'\n')
	

firstFileObject.close()
secondFileObject.close()
employee.close()
	
	
