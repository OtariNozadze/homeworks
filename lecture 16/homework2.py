class Student:
    courses = ["Mathematics", "Biology", "Geography", "Literature", "Physics", "Art"]
    @classmethod
    def see_courses(cls):
         print(f"Registrable courses: {', '.join(cls.courses)}")

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.course = set()

    def register_courses(self, course):
        if course in Student.courses:
            self.course.add(course)
        else:
            print("That Course is Not Registrable")

    def student_info(self):
            if self.course:
                print(f"Student Name: {self.name}\n"
                      f"Student ID: {self.student_id}\n"
                      f"Student Courses: {', '.join(self.course)}")
            else:
                print(f"Student Name: {self.name}\n"
                      f"Student ID: {self.student_id}\n"
                      f"Student Courses: This student is Not Registered in any Courses")


Student.see_courses()

student_1 = Student("student_1", 3)
student_1.register_courses("Mathematics")
student_1.register_courses("Literature")
student_1.student_info()

student_2 = Student("student_2", 8)
student_2.register_courses("Geography")
student_2.register_courses("Art")
student_2.register_courses("Biology")
student_2.student_info()

