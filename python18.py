class Department:

    def __init__(self,student_name):
        self.student_name = student_name

    def details(self):
        return "Student Details"

class CSE(Department):

     def details(self):
         return f"{self.student_name}:CSE Department"

class IT(Department):

    def details(self):
        return f"{self.student_name}:IT Department"

class Student(CSE):

     def __init__(self, student_name, project):

         super().__init__(student_name)

         self.project = project

     def show_project(self):
        return f"{self.student_name} is doing {self.project} project"

s1 = CSE("Abi")
s2 = IT("Hari")
s3 = Student("dhanu","project_name")

print(s1.details())
print(s2.details())
print(s3.details())
print(s3.show_project())

