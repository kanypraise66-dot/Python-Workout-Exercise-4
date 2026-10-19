class Hello:

    def __init__(self, age, name):
        self.age = age
        self.name = name
        print(f"Hello my name is {name}, and I am {age} years old .")

        return


age = input("Enter age: ")
name = input("Enter name: ")

Hello(age, name)
