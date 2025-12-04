from Printer import *

class PrintDispatcher:
    def __init__(self, number_of_printers):
        self.printers = [Printer(i+1) for i in range(number_of_printers)]
        self.semaphore = threading.Semaphore(number_of_printers)

    def send_to_print(self, requirement):
        with self.semaphore:
            selected_printer = None

            for printer in self.printers:
                if not printer.is_busy:
                    selected_printer = printer
                    break

            if selected_printer:
                selected_printer.print_file(requirement)