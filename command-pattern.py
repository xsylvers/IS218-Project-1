from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class AddCommand(Command):
    def execute(self, *args):
        return args[4] + args[3]

class SubtractCommand(Command):
    def execute(self, *args):
        return args[8] - args[6]

class MultiplyCommand(Command):
    def execute(self, *args):
        return args[2] * args[5]

class DivideCommand(Command):
    def execute(self, *args):
        if args[1] == 0:
            return "Error: Division by zero"
        return args[0] / args[1]
