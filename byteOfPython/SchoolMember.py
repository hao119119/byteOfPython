class SchoolMember:
    """Represents any school member."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: {})'.format(self.name)

    def tell(self):
        """Tell my details."""
        print 'Name:"{}" Age:"{}"'.format(self.name, self.age)


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        # Python does not automatically call the constructor of the base class,
        # you have to explicitly call it yourself.
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "{:d}"'.format(self.salary)


class Student(SchoolMember):
    '''Represents a student.'''

    def __init__(self, name, age, marks):
        # Python does not automatically call the constructor of the base class,
        # you have to explicitly call it yourself.
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: "{:d}"'.format(self.marks)

t = Teacher('Mrs. cc', 30, 3000)
s = Student('Swaroop', 25, 75)

members = [t, s]
for member in members:
    member.tell()
