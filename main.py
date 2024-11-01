from dotenv import load_dotenv
import os
import logging
import logging.config

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
ENV = os.getenv('ENV')
SECRET_KEY = os.getenv('SECRET_KEY')

print(f'Environment: {ENV}')
print(f'Secret Key: {SECRET_KEY}')

# Load logging configuration from logging.conf
logging.config.fileConfig('logging.conf')

# Create a logger
logger = logging.getLogger()

# Example log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

from commands.add_command import AddCommand  # type: ignore
from commands.subtract_command import SubtractCommand  # type: ignore
from commands.multiply_command import MultiplyCommand  # type: ignore
from commands.divide_command import DivideCommand  # type: ignore
from calculator import Calculator  # Assuming the REPL logic and plugin loader are in calculator.py

if __name__ == "__main__":
    # Log that the calculator application is starting
    logger.info("Starting the calculator application.")

    calc = Calculator()
    calc.register_command('add', AddCommand())
    calc.register_command('subtract', SubtractCommand())
    calc.register_command('multiply', MultiplyCommand())
    calc.register_command('divide', DivideCommand())
    
    calc.load_plugins()  # This line of code loads up any additional plugins dynamically
    calc.repl()          # This line of code starts up the REPL

    # Log that the REPL is now running
    logger.info("REPL is now running.")
