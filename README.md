# forced-type-hints
It basically allows you to force types I mean, using decorator,
the function itself would throw an error if unexpected 
type was given compared with the set typehint on parameter 

### Example
```
from typing import get_type_hints

def forced_type(func):
    def inner(*args, **kwargs):
        th = get_type_hints(func)
        for index, (arg, typ) in enumerate(zip(args, th.values())):
            if not isinstance(arg, typ):
                raise ValueError(f'{arg} must be {typ}')
        
        for val, typ in zip(kwargs, list(th.values())[len(args):]):
            if not isinstance(val, typ):
                raise ValueError(f'{val} must be {typ}')
            
        
        return func(*args, **kwargs)
    return inner 
    
@forced_type
def add(n1: int, n2: int):
    return n1 + n2
    
print(add(2, 2)) # 4 
    
```

### :warning: Note :warning: 
All variables gotta follow a typehint otherwise it'd not work well
