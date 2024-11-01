from . import Plugin

class DividePlugin(Plugin):
    def execute(self, calculator, x, y):
        return calculator.divide(x, y)
