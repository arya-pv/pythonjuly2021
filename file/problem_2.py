class Student:
    def __init__(self,name,roll_no,course,marks):
        self.name=name
        self.roll_no=roll_no
        self.course=course
        self.marks=marks
    def print(self):
        print(self.name)
        print(self.roll_no)
        print(self.course)
        print(self.marks)
f2=open("student_2","r")
for line in f2:
    l=line.split(",")
    name=l[0]
    roll_no=l[1]
    course=l[2]
    marks=l[3]
    st=Student(name,roll_no,course,marks)
    st.print()