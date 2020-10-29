# This is a simple function; no automatic self here
def my_function(stranger, name):
  my_name = 12    # local variable
  print("Hello, {}!  My name is {}".format(stranger, name))
  print(my_name)

# This is a class
class Student:
  # This is the method; it has self passed automatically
  def hello(self, stranger):
    print("Hello, {}!  My name is {}".format(stranger, self.name))

  def __init__(self, name):  # constructror
    self.name = name
    self.age = 1
    self.male = True

  # this is a static method; if outside a class, it's called a plain function
  def static_method():
    print("Static method: look ma! No self; I can be called without any object")

def NewFunc():
  new_student = Student("Visu")
  new_student.hello("lshdf")
  Student.static_method()

# Calling plain function
NewFunc()

s1 = Student("abc")  # instantiation: creating object from class
s = []
s.append(Student("Selva"))
s.append(Student("Sundaram"))
s.append(Student("Skandha"))

for i in range(3):
  my_function("Kumar", "Selva")

s[2].hello("Kumar")
print(s[0].age)