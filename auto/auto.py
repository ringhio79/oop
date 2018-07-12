class Auto:
    pass
    
class Engine:
    def __init__(self, engine_type, capacity=0):
        self.engine_type = engine_type.lower()
        self.capacity = capacity
        
    def start(self):
        return 'vroom vroom!'
    
    def stop(self):
        return 'engine stopped'

class Wheel:
    def __init__(self, size, tyre_type):
        self.size = size
        self.tyre_type = tyre_type
        
    def rotate(self):
        return 'Turning!'
        
    def stop(self):
        return 'Braking!'

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
    def __init__(self, composition, is_soft_top=False, is_articulated=False):
        self.composition = composition
        self.is_soft_top = is_soft_top
        self.is_articulated = is_articulated
        
    def open_roof(self):
        if self.is_soft_top == True:
            return 'whirr..... fold.... clunk'
        else:
            return 'cannot open roof'
            
    def close_roof(self):
        if self.is_soft_top == True:
            return 'unfold .... whirr... clunk'
        else:
            return 'no roof to close'
