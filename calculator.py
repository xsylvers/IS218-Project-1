import pandas as pd
import os
import logging

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        result = x + y
        self.history.append({'operation': 'add', 'input': (x, y), 'result': result})
        return result

    def subtract(self, x, y):
        result = x - y
        self.history.append({'operation': 'subtract', 'input': (x, y), 'result': result})
        return result

    def multiply(self, x, y):
        result = x * y
        self.history.append({'operation': 'multiply', 'input': (x, y), 'result': result})
        return result

    def divide(self, x, y):
        if y == 0:
            logging.error("Attempted division by zero.")
            return "Error: Division by zero"
        result = x / y
        self.history.append({'operation': 'divide', 'input': (x, y), 'result': result})
        return result

    def get_history(self):
        return pd.DataFrame(self.history)

    def clear_history(self):
        self.history.clear()
