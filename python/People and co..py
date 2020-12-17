class Person:
    def __init__(self, fName, lName, dateOfBirth, gender="Not Specified", phoneNumber=None, address=None):
        self.fName = fName
        self.lName = lName
        self.dateOfBirth = dateOfBirth
        self.gender = gender
        self.phoneNumber = phoneNumber
        self.address = address

    def getData(self, dataType):
        if dataType == "First Name": return self.fName
        if dataType == "Last Name": return self.lName
        if dataType == "Date of Birth": return self.dateOfBirth
        if dataType == "Gender": return self.gender
        if dataType == "Phone Number": return self.phoneNumber
        if dataType == "Address": return self.address


class Student(Person):
    def __init__(self, fName, lName, dateOfBirth, gender="Not Specified", phoneNumber=None, address=None):
        super().__init__(self, fName, lName, dateOfBirth, gender, phoneNumber, address)


if __name__ == "__main__":
    p1 = Person("John", "Muffin", "01/12/2015", "M", "0791727478", "11 Downing Street")
    print(p1.getData("First Name"))
