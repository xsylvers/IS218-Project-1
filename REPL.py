class Calculator:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, name, *args):
        if name in self.commands:
            return self.commands[name].execute(*args)
        else:
            return f"Unknown command: {name}"

    def repl(self):
        print("Welcome to my interactive calculator! Type 'exit' if you choose quit.")
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
