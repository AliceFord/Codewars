class Person:
    def __init__(self, name, age): # Constructor
        self.name = name
        self.age = age
    
    def outputNameAndAge(self):
        print("My name is {}, and I am {}.".format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, graduationYear):
        super().__init__(name, age)
        self.graduationYear = graduationYear
    
    def welcomeToClass(self):
        print("Welcome, {} to the class that graduates in {}.".format(self.name, self.graduationYear))

p1 = Person("John", 43)
p1.outputNameAndAge()
print(p1.age)
p2 = Student("Jim", 20, 1991)
p2.welcomeToClass()
print(p2.name)