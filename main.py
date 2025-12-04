from Requirement import *
from PrintDispatcher import *

requirements = []

def create_requirement(count, path):
    new_requirement = Requirement(count, path)
    requirements.append(new_requirement)

if __name__ == "__main__":
    dispatcher = PrintDispatcher(3)
    count = 0

    while True:
        count += 1
        path = input("")

        if path == "exit":
            break

        create_requirement(count, path)
        t = threading.Thread(target=dispatcher.send_to_print, args=(requirements[0],))
        t.start()

        requirements.remove(requirements[0])