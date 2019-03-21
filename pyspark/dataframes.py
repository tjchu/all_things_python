# import pyspark class Row from module sql
from pyspark.sql import *


# Create Example Data - Departments and Employees

# Create the Departments
department1 = Row(id='123456', name='Computer Science')
department2 = Row(id='789012', name='Mechanical Engineering')
department3 = Row(id='345678', name='Theater and Drama')
department4 = Row(id='901234', name='Indoor Recreation')

# Create the Employees
Employee = Row("firstName", "lastName", "email", "salary")
employee1 = Employee('Michael', 'Scott', 'no-reply@berkeley.edu', 100000)
employee2 = Employee('Dwight', 'Schrute', 'no-reply@stanford.edu', 120000)
employee3 = Employee('Terry', 'Chu', 'no-reply@waterloo.edu', 140000)
employee4 = Employee('Mark', 'Zuckerberg', 'no-reply@berkeley.edu', 160000)

# Create the DepartmentWithEmployees instances from Departments and Employees
departmentWithEmployees1 = Row(department=department1, employees=[employee1, employee2])
departmentWithEmployees2 = Row(department=department2, employees=[employee3, employee4])
departmentWithEmployees3 = Row(department=department3, employees=[employee1, employee4])
departmentWithEmployees4 = Row(department=department4, employees=[employee2, employee3])

print(department1)
print(employee2)
print(employee1.firstName, employee1.lastName)
print(departmentWithEmployees1.employees[0].firstName)

# Create DataFrames from a list of rows
"""departmentsWithEmployeesSeq1 = [departmentWithEmployees1, departmentWithEmployees2]
df1 = sc.createDataFrame(departmentsWithEmployeesSeq1)

display(df1)

departmentsWithEmployeesSeq2 = [departmentWithEmployees3, departmentWithEmployees4]
df2 = sc.createDataFrame(departmentsWithEmployeesSeq2)

display(df2)"""

