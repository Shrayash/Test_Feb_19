class Student:
    def __init__(self, student_name, student_sec):
        self.student_name = student_name
        self.student_sec = student_sec

    @classmethod
    def gen_student_from_string(cls, inp):
        student_name, student_sec = inp.split("-")
        return cls(student_name, student_sec)


students = Student.gen_student_from_string("Shrayash-B")

print(students.__dict__)