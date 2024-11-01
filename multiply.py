from . import Plugin

class MultiplyPlugin(Plugin):
    def execute(self, calculator, x, y):
        return calculator.multiply(x, y)
