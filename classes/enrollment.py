class Enrollment:
    def __init__(self, term, student, course):
        self.term = term
        self.student = student
        self.course = course

        @property
        def term(self):
            return self._term
        
        @property
        def student(self):
            return self._student
        
        @property
        def course(self):
            return self._course
        
        @term.setter
        def term(self, term):
            
            if term[0] == 'F' or term[0] == 'S' and term[-4:].isdigit():
                self._term = term
            else:
                raise Exception("That's not the correct format for a term!")
            
        @student.setter
        def student(self, student):
            from student import Student
            STUDENT_TYPE = isinstance(student, Student)
            if STUDENT_TYPE:
                self._student = student

        @course.setter
        def course(self, student):
            from course import Course
            COURSE_TYPE = isinstance(course, Course)
            if COURSE_TYPE:
                self._course = course

        
        