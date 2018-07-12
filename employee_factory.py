from employees.employee import Employee, Developer, SalesPerson, Ceo

my_employee = Employee('Tim', 'Tipple', 30)

print(my_employee.fname) 
print(my_employee.calc_salary())
print(my_employee.get_details())

my_coder = Developer('Tweety', 'Bird', 2, 'python')

print(my_coder.lang)
print(my_coder.fname)
print(my_coder.calc_salary())
print(my_coder.get_details())


one_sales = SalesPerson('Minnie', 'Mouse', 6, 'emea')

print(one_sales.fname)
print(one_sales.territory)
print(one_sales.get_details())

my_ceo = Ceo('walt', 'Disney', 30, True)

print(my_ceo.sname)
print(my_ceo.calc_salary())