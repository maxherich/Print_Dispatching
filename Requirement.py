import time

class Requirement:
    def __init__(self, number, path):
        self.number = number
        self.path = path

    def execute(self):
        print(f"Requirement {self.number} is being printed")
        time.sleep(3)
        with open(f"./Printed/print{self.number}.txt", "w") as file:
            file.write(f"Print number {self.number}")