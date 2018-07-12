from employees.employee import Employee

my_employee = Employee('Tim', 'Tipple', 4)

print(my_employee.fname) 

print(my_employee.calc_salary())

print(my_employee.get_details())

sec_employee = Employee('Mickey', 'Mouse', 30)

print(sec_employee.nyears)
print(sec_employee.get_details())

thir_employee = Employee('Duffy', 'Duck', 2)

print(thir_employee.sname)
print(thir_employee.get_details())
