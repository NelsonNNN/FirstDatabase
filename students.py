class Students():
    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks

    def email(self):
        return '{}{}@gmail.com'.format(self.first, self.last)
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def details(self):
        return 'Student: {}, {}, {}'.format(self.first, self.last, self.marks)