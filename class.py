def method_name(a, b):
    print("A method")

class Person:
    def _init_(self, person_name):
        self.name = person_name

    def get_name(self):
        return self.name

method_name(10, 20)
a_person = Person("shahadat")
b_person = Person("Robot")

print(a_person.get_name())
print(b_person.get_name())
