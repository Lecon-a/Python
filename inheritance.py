'''
Inheritance enables us to define a class that inherits methods and properties of another class.

Parent/base class is the class being inherited from. While, child/derived class is the class that inherits from another class.
'''


class Student():
    def __init__(self, lname, fname, mname, admissionDate):
        self.lname = lname
        self.fname = fname
        self.mname = mname
        self.admissionDate = admissionDate

    def welcome(self):
        print("Welcome", self.fname, self.lname,
              "to the class of")


class UnderGraduate(Student):
    def __init__(self, lname, fname, mname, admissionDate, graduationYear):
        super().__init__(lname, fname, mname, admissionDate)
        self.graduationYear = graduationYear

    def welcome(self):
        print("Welcome", self.fname, self.lname,
          "to the class of", self.graduationYear)



class PostGraduate(Student):
    def __init__(self, lname, fname, mname, admissionDate, graduationYear):
        Student.__init__(self, lname, fname, mname, admissionDate)
        self.graduationYear = graduationYear

    def welcome(self):
        print("Welcome", self.fname, self.lname,
              "to the class of", self.graduationYear)

        


postgraduate = PostGraduate("Afolabi", "Sunday", "Peter", "2023", 0)
undergraduate = UnderGraduate("Afolabi", "Sunday", "Peter", "2015", 2019)

postgraduate.welcome()
undergraduate.welcome()
