class person:
    def set_person(self,name,age):
        self.name=name
        self.age=age
    def print_person(self):
        print(self.name)
        print(self.age)
obj=person()
obj.set_person("vishnu",25)
obj.print_person()

obj1=person()
obj.set_person("Ajith",25)
obj.print_person()