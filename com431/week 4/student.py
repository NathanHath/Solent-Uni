class Student:
    def __init__(self, ID, name, course, mark):
        self.ID = ID
        self.name = name
        self.course = course
        self.mark = mark

    def __str__(self):
        return f"student ID:{self.ID}, student name:{self.name}, student course:{self.course}, mark:{self.mark}"

    def __repr__(self):
        return self.__str__()

    def set_Mark(self, mark):
        if 0 <= self.mark <= 100:
            self.mark = mark
        else:
            raise Exception ("Invalid mark")

    def set_grade(self, grade, mark):
        if mark <= 70:
            return "70+ : First"
        elif mark <= 60:
            return "60-69 : 2/1"
        elif mark <= 50:
            return "50-59 : 2/2"
        elif mark <= 40:
            return "40-49 : Third"
        else:
            return "0-39 : Fail"
