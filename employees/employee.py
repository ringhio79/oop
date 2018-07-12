class Employee(object):
    
    BASE_SALARY = 50000
    fname = ''
    sname = ''
    nyears = '0'
    
    def __init__(self, first_name, second_name, number_years):
        self.fname = first_name
        self.sname = second_name
        self.nyears = number_years
        
    def calc_salary(self):
        if self.nyears < 3:
            return self.BASE_SALARY*1.01
        elif self.nyears <= 5:
            return self.BASE_SALARY*1.10
        elif self.nyears > 5:
            return self.BASE_SALARY*1.25
            
            
    def get_details(self):
        return '{0} {1} worked for: {2} years salary is: {3}'.format(self.fname, self.sname, self.nyears, self.calc_salary())
        
class Developer(Employee):
    lang = ''
    
    def __init__(self, first_name, second_name, number_years, language):
        super(Developer, self).__init__(first_name, second_name, number_years)
        self.lang = language.lower()
        
    def calc_salary(self):
        salary = super(Developer, self).calc_salary()
        if self.lang == 'python':
            salary =  salary + 500
        elif self.lang == 'java':
            salary = salary + 300
        elif self.lang == 'none':
            salary = 'No language bonus'
        return salary
            
    def get_details(self):
        return '{0} {1} worked for: {2} years salary is: {3}'.format(self.fname, self.sname, self.nyears, self.calc_salary())

class SalesPerson(Employee):
    territory = ''
    
    
    def __init__(self, first_name, second_name, number_years, geo_territory):
        super(SalesPerson, self).__init__(first_name, second_name, number_years)
        self.territory = geo_territory.upper()
        
    def calc_salary(self):
        salary = super(SalesPerson, self).calc_salary()
        if self.territory == 'EMEA':
            salary =  salary + 1000
        elif self.territory == 'APAC':
            salary = salary + 800
        elif self.territory == 'US':
            salary = salary + 1500
        return salary
            
    def get_details(self):
        return '{0} {1} worked for: {2} years salary is: {3}'.format(self.fname, self.sname, self.nyears, self.calc_salary())
        
class Ceo(Employee):
    growth = True
    
    def __init__(self, first_name, second_name, number_years, positive_growth):
        super(Ceo, self).__init__(first_name, second_name, number_years)
        self.growth = positive_growth
        
    def calc_salary(self):
        salary = super(Ceo, self).calc_salary()
        if self.growth == True:
            salary =  salary + 2000
        elif self.growth == False:
            salary = salary - 100
        return salary
            
    def get_details(self):
        return '{0} {1} worked for: {2} years salary is: {3}'.format(self.fname, self.sname, self.nyears, self.calc_salary())
         
        