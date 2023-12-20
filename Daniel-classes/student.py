class Student:
    def __init__(self, name, grad_year, gpa) -> None:
        self.name: str = name
        self.grad_year:int = grad_year
        self.gpa: float = gpa
        

        self.enrollment_list = []
    @property
    def enrollment_list(self):
        return self._enrollment_list
    @enrollment_list.setter
    def enrollment_list(self, enrollment_list):
        if hasattr(self, "enrollment_list"):
            raise Exception("can't reassign enrollment_list")
        self._enrollment_list = enrollment_list

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if len(name.split()) < 2:
            raise ValueError("Name must have at least a first name and a last name")
        self._name = name

    @property
    def grad_year(self):
        return self._grad_year
    
    @grad_year.setter
    def grad_year(self, grad_year):
        if grad_year < 2024:
            raise Exception("Grad year can't in the past")
        self._grad_year = grad_year

    @property
    def gpa(self):
        return self._gpa
    
    @gpa.setter
    def gpa(self, gpa):
        # if 0.0 > gpa or gpa  > 4.0:
        #     raise Exception("gpa must be between 0.0 and 4.0")
        # self._gpa = gpa
        if 0.0 <= gpa <= 4.0:
            self._gpa = gpa
        else:
            raise Exception("gpa must be between 0.0 and 4.0")
        
    def count_instructors(self):
        instructor_set = set()
        for e in self.enrollment_list:
            instructor_set.add(e.course.instructor)
        return len((instructor_set))
    


# s.enrollment_list.append("test")
