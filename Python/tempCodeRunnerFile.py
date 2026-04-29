class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sample(self,place):
            print(f"My name is {self.name} and My age is {self.age} and my place is{place}")
s1=student("satya",20)
s1.sample("USA")