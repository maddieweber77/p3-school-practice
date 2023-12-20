from student import Student
from course import Course

class Enrollment:
    
    '''
    Attributes:
        student object
        course object
        term 
    Properties:
        student must be of type Student
        course must be of type Course
        term must start with 'F' or 'S' and end with 4 digits
    '''
    def __init__(self, student, course, term) -> None:
        self.student = student
        self.course = course
        self.term = term

        course.enrollment_list.append(self)
        student.enrollment_list.append(self)

    @property
    def student(self):
        return self._student
    @student.setter
    def student(self, student):
        from student import Student
        if not isinstance(student, Student):
            raise Exception("student must be instance of Student")
        self._student = student

    @property
    def course(self):
        return self._course
    @course.setter
    def course(self, course):
        from course import Course
        if not isinstance(course, Course):
            raise Exception("course must be instance of Course")
        self._course = course

    @property
    def term(self):
        return self._term
    
    @term.setter
    def term(self,term):
        if term[0] not in ['S' , 'F'] or not term[-4:].isdecimal():
            raise Exception("term must be in format [S|F]YEAR")
        self._term = term

s1 = Student("Lohan Myles", 2024, 4.0)
s2 = Student("Bartleby Branson", 2024, 3.1)
s3 = Student("Elmo Crump", 2025, 3.1)

c1 = Course( "Guy Steele","Java")
c2 = Course( "Guy Steele","Lisp")
print(Course.titles)

Enrollment(student=s1,course=c1, term="S2024")
Enrollment(student=s2,course=c1, term="S2024")
Enrollment(student=s3,course=c1, term="S2024")
Enrollment(student=s1,course=c2, term="S2024")
print(c1.get_most_common_grad_year())