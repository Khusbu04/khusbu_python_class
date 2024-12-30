class Person: ## blueprint
    def _init_(self, name, age): ## dunder method or magic : self call, _init_: runs when object create
        self.name = name
        self.age = age
    #def _int_(self):
    #   pass
    # pass
khusbu = Person("Khusbu", 19)
print(khusbu.name)
print(khusbu.age)