class LoggingMeta(type):
    def __new__(cls, name, bases, class_dict):
        print(f"Class Name: {name}")
        instance = super().__new__(cls, name, bases, class_dict)
        return instance
    
class FirstClass(metaclass=LoggingMeta):
    pass

class SecendClass(metaclass=LoggingMeta):
    pass
    






