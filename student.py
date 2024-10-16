
class Student:
  count=0
  def __init__(self,name,email,address,marks):
     self.name= name
     self.email= email
     self.address=address
     self.marks= marks
     self.avg= sum(self.marks)/len(self.marks)
     Student.count +=1

def check_pass_fail(self):
  if self.avg >= 50:
    return "pass"
  else:
    return "Fail"
def display(self):
   print(f"name:{self.name},email:{self.email},address:{self.address},mark:{self.marks}, average: {self.avg}, result: {self.check_pass_fail()}")


from student import Student
students=[]

def getMarks():
    marks=[]
    subCount=1
    while True:
        mark=int(input(f"Enter Subject{subCount}mark:"))
        marks.append(mark)
        subCount += 1
        flag = input("Do you want to cotinue (YES/NO)?")
        if flag!='YES':
            break
    return marks

def getStudentInfo():
 name =input("Enter your name:")
 email =input("Enter your email:")
 address=input("Enter your address:")
 marks=getMarks()
 student= Student(name,email,address,marks)
 students.append(student)

while True:
 getStudentInfo()
 flag=input("do you want to continue(Yes/No)?")
 if flag!="YES":
   break
for student in students:
  student.display()

print(f"Total student count{Student.count}")



