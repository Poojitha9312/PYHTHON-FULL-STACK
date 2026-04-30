class satya:
    def __init__(x):
        x.name=input("Please enter your name:")
        x.age=int(input("please enter your age:"))
    def sample(x):
        print(f"My name is {x.name} and My age is{x.age}")
a=satya()
a.sample()