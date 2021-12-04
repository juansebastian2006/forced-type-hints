from typing import get_type_hints

def forced_type(func):
    def inner(*args, **kwargs):
    
        th = get_type_hints(func) # a dictionary with variables as keys and the type as values
        
        for index, (arg, typ) in enumerate(zip(args, th.values())):
            if not isinstance(arg, typ):
                raise ValueError(f'{arg} must be {typ}')
        
        for val, typ in zip(kwargs, list(th.values())[len(args):]):
            if not isinstance(val, typ):
                raise ValueError(f'{val} must be {typ}')
            
        
        return func(*args, **kwargs) # it just does its function 
    return inner 
