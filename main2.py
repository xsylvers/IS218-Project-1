import importlib
import os
import logging
from calculator import Calculator
from history_management import HistoryManagement
from logging_config import LOG_LEVEL

def load_plugins():
    plugins = {}
    for filename in os.listdir('plugins'):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            module = importlib.import_module(f'plugins.{module_name}')
            class_name = module_name.capitalize() + 'Plugin'
            plugin_class = getattr(module, class_name)
            plugins[class_name] = plugin_class()
    return plugins

def main():
    calculator = Calculator()
    history_manager = HistoryManagement()
    plugins = load_plugins()

    # Load history on startup
    history = history_manager.load_history()

    while True:
        command = input("Enter command (or 'help' for options): ").strip()
        if command.lower() == 'exit':
            break
        elif command.lower() == 'history':
            print(history)
        elif command.lower() == 'clear history':
            calculator.clear_history()
            history_manager.clear_history()
            print("History cleared.")
        elif command.lower() == 'help':
            print("Available commands: add, subtract, multiply, divide, history, clear history, exit")
        else:
            try:
                parts = command.split()
                if len(parts) == 3:
                    operation, x, y = parts[0], float(parts[1]), float(parts[2])
                    if operation in plugins:
                        result = plugins[operation.capitalize() + 'Plugin'].execute(calculator, x, y)
                    else:
                        print("Unknown command. Type 'help' for options.")
                else:
                    print("Invalid command format.")
            except Exception as e:
                logging.error(f"Error occurred: {e}")
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
