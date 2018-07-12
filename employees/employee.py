class Employee(object):
    
    BASE_SALARY = 5000
    fname = ''
    sname = ''
    nyears = '0'
    
    def __init__(self, first_name, second_name, number_years):
        self.fname = first_name
        self.sname = second_name
        self.nyears = number_years
        
    def calc_salary(self):
        if self.nyears < 3:
            return 'salary is {0}'.format(self.BASE_SALARY*1.01)
        elif self.nyears <= 5:
            return 'salary is {0}'.format(self.BASE_SALARY*1.10)
        elif self.nyears > 5:
            return 'salary is {0}'.format(self.BASE_SALARY*1.25)
            
            
    def get_details(self):
        return '{0} {1} has worked for {2} years and {3}'.format(self.fname, self.sname, self.nyears, self.calc_salary())
        
        