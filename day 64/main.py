class job:
  name = None
  salary = None
  hoursWorked = None

  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")

class doctor(job):
  experience = None
  speciality = None

  def __init__(self, salary, hoursWorked, experience, speciality):
    self.name = "Doctor"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.experience = experience
    self.speciality = speciality

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.experience:<10} {self.speciality:>21}")

class teacher(job):
  subject = None
  position = None

  def __init__(self, salary, hoursWorked, subject,  position):
    self.name = "Teacher"
    self.hoursWorked = hoursWorked
    self.salary = salary
    self.subject = subject
    self.position = position
  
  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.subject:<10} {self.position:>21}")

lawyer = job("Lawyer", "$100,000", "40")
lawyer.print()

doc = doctor("$120,000", "48", "7", "Pediatric Consultant")
doc.print()

teach = teacher("$50,000", "48+", "CompSci", "Asst. Principal")
teach.print()
'''
class Job:
  name = None
  salary = None
  hoursWorked = None

  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")

class Doctor(Job):
  experience = None
  speciality = None

  def __init__(self, salary, hoursWorked, experience, speciality):
    super().__init__(salary, hoursWorked)
    self.experience = experience
    self.speciality = speciality

  def print(self):
    super().print()
    print(f"{self.experience:<10} {self.speciality:>21}")

class Teacher(Job):
  subject = None
  position = None

  def __init__(self, salary, hoursWorked, subject,  position):
    super().__init__(salary, hoursWorked)
    self.subject = subject
    self.position = position
  
  def print(self):
    super().print()
    print(f"{self.subject:<10} {self.position:>21}")

lawyer = Job("Lawyer", "$100,000", "40")
lawyer.print()

doc = Doctor("$120,000", "48", "7", "Pediatric Consultant")
doc.print()

teach = Teacher("$50,000", "48+", "CompSci", "Asst. Principal")
teach.print()

'''
'''
class Job:
    def __init__(self, name, salary, hours_worked):
        self.name = name
        self.salary = salary
        self.hours_worked = hours_worked

    def print_info(self):
        print("== JOB ==")
        print()
        print(f"{self.name:<10} {self.salary:^10} {self.hours_worked:>10}")

class Doctor(Job):
    def __init__(self, salary, hours_worked, experience, speciality):
        super().__init__("Doctor", salary, hours_worked)
        self.experience = experience
        self.speciality = speciality

    def print_info(self):
        super().print_info()
        print(f"{self.experience:<10} {self.speciality:>21}")

class Teacher(Job):
    def __init__(self, salary, hours_worked, subject, position):
        super().__init__("Teacher", salary, hours_worked)
        self.subject = subject
        self.position = position

    def print_info(self):
        super().print_info()
        print(f"{self.subject:<10} {self.position:>21}")

lawyer = Job("Lawyer", "$100,000", "40")
lawyer.print_info()

doc = Doctor("$120,000", "48", "7", "Pediatric Consultant")
doc.print_info()

teach = Teacher("$50,000", "48+", "CompSci", "Asst. Principal")
teach.print_info()
'''

