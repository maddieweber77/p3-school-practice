class Course:
    '''
    Attributes:
        instructor
        title
        enrollment_list
    Properties:
        title must not be duplicated for any courses (hint: class attribute)
    Methods:
        get_average_gpa_of_enrolled_students: returns the average
        gpa of all students enrolled in that course

        get_most_common_grad_year: returns the year that has the most
        students graduating who are enrolled in that course
    '''
    titles = set()
    def __init__(self, instructor, title) -> None:
        self.instructor = instructor
        self.title = title

        self.enrollment_list = []

        pass
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if title in Course.titles:
            raise Exception("Can't duplicate titles")
        Course.titles.add(title)
        self._title = title

    def get_average_gpa_of_enrolled_students(self):
        # total_gpa = 0
        # length = 0
        # for enrollment in self.enrollment_list:
        #     total_gpa += enrollment.student.gpa
        #     length += 1
        # return total_gpa / length
        gpa_list = [enrollment.student.gpa for enrollment in self.enrollment_list ]
        return sum(gpa_list)/ len(gpa_list)
    # [1,2,2,3]
    #  1 2   1
    def get_most_common_grad_year(self):
        grad_year_list = [enrollment.student.grad_year for enrollment in self.enrollment_list ]
        return max(grad_year_list, key=grad_year_list.count)

