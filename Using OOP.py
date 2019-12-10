#------------------------------------------------
#Dylan Friesen
#Using OOP Assignment
#Monday December 9
#------------------------------------------------

class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.ca'
        
    def fullname(self):
        return format(self.first, self.last, self.email)

class Principal(Student):
    def __init__(self, first, last):
        super().__init__(first, last)
        
student = Student('Dylan', 'Friesen')
principal = Principal('Kyle', 'Wood')

print(student.email)
print(principal.email)

print(student.first + ' ' + principal.last)
print('How much', principal.last, 'could a', principal.last, 'chuck chuck if a', principal.last, 'chuck could chuck', principal.last,'.')
print('Created by', student.first, student.last,'.', 'You can find him at', student.email,'.')
    
    