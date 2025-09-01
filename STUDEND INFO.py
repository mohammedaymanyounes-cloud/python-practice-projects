
class student():
  def __init__(self,first_name,last_name,grades,status="student"):
    self.first_name=first_name
    self.last_name=last_name
    self.grades=grades
    self.status=status
  def show(self):
    print(f"student first name: {self.first_name}")
    print(f"student last name: {self.last_name}")
    print(f"grades: {self.grades}")
    print(f"status: {self.status}")
def create_acount():
  first_name=input("Enter your first name")
  last_name=input("Enter your last name")
  grades=input("Enter your grades ")
  return student(first_name,last_name,grades,)
student_1=create_acount()
student_1.show()

