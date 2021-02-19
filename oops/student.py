class student:
    def set_student(self,roll,name,total):
        self.roll=roll
        self.name=name
        self.total=total
    def print_student(self):
        print(self.roll)
        print(self.name)
        print(self.total)
student1=student()
student1.set_student(101,"Vishnu",495)
student1.print_student()

student2=student()
student2.set_student(102,"Shino",455)
student2.print_student()