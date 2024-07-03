class Student:
    def __init__(self, name, usn, m1,m2,m3):
        self.name = name
        self.usn = usn
        self.m1 = m1
        self.m2 = m2

        self.m3 = m3


    def __str__(self):
        return f"Name: {self.name}, USN: {self.usn}, Mark1: {self.m1},Mark2: {self.m2},Mark3: {self.m3}"

st_dict = {}

num = int(input("Enter the number of student"))

for i in range(num):
    name = input(f"Enter name for student {i+1}: ")
    age = input(f"Enter usn for student {i+1}: ")
    m1 = input(f"Enter marks of student subject 1: ")
    m2 = input(f"Enter marks of student subject 2: ")
    m3 = input(f"Enter marks of student subject 3: ")

    student = Student(name, age, m1,m2,m3)
    st_dict[f"Student {i+1}"] = student

print("\nStudents are :")
for key, student in st_dict.items():
    print(f"{key}: {student}")
