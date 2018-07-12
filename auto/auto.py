class Auto:
    pass
    
class Engine:
    pass

class Wheel:
    pass

class Door:
    def __init__(self, operation_type):
        self.operation_type = operation_type.lower()
    
    def open(self):
        if self.operation_type == 'automatic':
            return 'Click Swish!'
        else:
            return 'Click!'
    
    def close(self):
        if self.operation_type == 'automatic':
            return 'Swish Clunk'
        else:
            return 'Creak Clunk!!'

class Body:
    def __init__(self, composition, is_soft_top=False, is_articulated=False)
