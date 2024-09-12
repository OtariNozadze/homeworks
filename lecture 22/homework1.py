import pickle
import json
import dill

class SerializationError(Exception):
    pass

class Student():
    def __init__(self, name, last_name, birth_year, score):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.score = score

student1 = Student("Jhon", "Doe", 1989, 180)
student2 = Student("Kate", "White", 2000, 160)
student3 = Student("Alex", "Morgan", 1999, 100)


def serialization_formats(obj):
    try:
        data = json.dumps(obj)
        print("json")
        return data
    except:
        try:
            data = pickle.dumps(obj)
            print("pickle")
            return data
        except:
            try:
                data = dill.dumps(obj)
                print("dill")
                return data
            except:
                raise SerializationError("Failed to serialize the object with all formats")

print(serialization_formats(student2))
        



