class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        return f"{self.name} and his age {self.age}"
    
s1 = student("Anoop", 30)
s2 = student("Riya",29)

print(s1.show_info())
print(s2.show_info())