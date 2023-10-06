import os
import json
import commands
import re

class Main():
    def __init__(self):
        super().__init__()
        self.math_pattern = re.compile(r'^\s*\d+(\.\d+)?(\s*[\+\-\*/]\s*\d+(\.\d+)?)*\s*$')
        self.user = os.getenv("USERNAME")
        with open('commandList.json', 'r') as file:
            self.command_functions = json.load(file)
        os.system("cls")

    def run(self):
        while True:
            try:
                self.command = input(f"{os.getcwd()} | {self.user} > ")
                self.base()
                if self.command == "exit":
                    break

            except KeyboardInterrupt:
                break

    def base(self):
        parts = self.command.split(" ", 1)
        command_name = parts[0]
        arguments = parts[1] if len(parts) > 1 else ""

        if command_name in self.command_functions:
            command_function_name = self.command_functions[command_name]
            if hasattr(commands, command_function_name):
                func = getattr(commands, command_function_name)
                try:
                    if arguments:
                        func(arguments)
                    else:
                        func()
                except TypeError:
                    print(f"ERROR: Invalid usage of '{command_name}' command.")
            else:
                print(f"ERROR: No command function defined for \"{command_name}\"")
        elif self.math_pattern.match(self.command):
            try:
                result = eval(self.command)
                print(result)
            except (ValueError, ZeroDivisionError, SyntaxError):
                print("ERROR: Invalid math operation.")
        elif self.command == "exit":
            pass
        elif any(c.isspace() for c in self.command) or self.command == "":
            pass
        else:
            print(f"ERROR: No command with name \"{command_name}\"")

if __name__ == "__main__":
    main_instance = Main()
    main_instance.run()
