class Plugin:
    def execute(self, calculator, x, y):
        raise NotImplementedError("Each plugin must implement the execute method.")
