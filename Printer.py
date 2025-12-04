import threading

class Printer:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
        self.lock = threading.Lock()

    def print_file(self, requirement):
        with self.lock:
            self.is_busy = True

            print(f"Printer {self.number} is printing Requirement {requirement.number}")
            requirement.execute()
            print(f"Printer {self.number} just printed Requirement {requirement.number}")

            self.is_busy = False
