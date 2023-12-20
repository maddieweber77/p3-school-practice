class Course:
    _unique_titles = set()

    def __init__(self, instructor, title):
        self.instructor = instructor
        self.title = title
        
        self.enrollment_list = []

        @property
        def title(self):
            return self._title
        
        @title.setter
        def title(self, value):
            #if title is not unique:
            if value in Course._unique_titles:
                raise Exception(f"Course with title '{value}' already exists.")
            # if title is unique
            self._title = value
            Course._unique_titles.add(value)

        @property
        def instructor(self):
            return self._instructor
        
        @instructor.setter
        def instructor(self, instructor):
            self._instructor = instructor

Class Enrollment:
    def __init__(self, student, course, term):
    self.student = student



C = Course("Maddie", "Python")
print(C.title)
        
        

        