import importlib
import os

class Calculator:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def load_plugins(self):
        plugin_folder = 'plugins'
        for filename in os.listdir(plugin_folder):
            if filename.endswith('_command.py'):
                module_name = filename[:-3]
                module = importlib.import_module(f"{plugin_folder}.{module_name}")
                command_class_name = ''.join([word.capitalize() for word in module_name.split('_')])
                command_class = getattr(module, command_class_name)
                self.register_command(module_name.split('_')[0], command_class())

    def execute_command(self, name, *args):
        if name in self.commands:
            return self.commands[name].execute(*args)
        else:
            return f"Unknown command: {name}"

    def repl(self):
        print("Welcome to my interactive calculator! Type 'exit' to quit.")
        while True:
            user_input = input("Enter command: ")
            if user_input == 'exit':
                break
            parts = user_input.split()
            command_name = parts[0]
            try:
                operands = list(map(float, parts[1:]))
                result = self.execute_command(command_name, *operands)
                print(f"Result: {result}")
            except ValueError:
                print("Error: Please provide valid numbers.")
