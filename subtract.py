from . import Plugin

class SubtractPlugin(Plugin):
    def execute(self, calculator, x, y):
        return calculator.subtract(x, y)
