from . import Plugin

class AddPlugin(Plugin):
    def execute(self, calculator, x, y):
        return calculator.add(x, y)
