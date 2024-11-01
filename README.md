# IS218-Project-1

**Table of Contents**

**1. Design Patterns**

- Facade Pattern
- Command Pattern
- Factory Method Pattern
- Singleton Pattern
- Strategy Pattern
   
   **Facade Pattern**: The Facade pattern is used in calculator.py to simplify complex operations on history management, data retrieval, and calculations. It hides the complex interactions with the Pandas DataFrame, offering a cleaner interface for other parts of the code.
  
  Description: The History Management class acts as a facade, providing methods to load, save, clear, and delete calculation history, abstracting away the complexities of data handling with Pandas
   
   **Command Pattern**: The Command pattern is used to encapsulate each basic command I used such as add, subtract, multiply, and divide as an object. This is especially useful for managing commands in the REPL interface.
  
  Description: Each operation (add.py, subtract.py and etc) is implemented as a separate command class. This allows the REPL to execute commands in a structured and 
 uniform way.
   
   **Factory Method**: The Factory Method pattern is used to create instances of commands dynamically. This approach makes it easy to add new command types in the future.

   Description: The command factory class is responsible for creating instances of command classes based on user input, making the code flexible and extensible.
   
   **Singleton**: The Singleton pattern is used for logging configuration to ensure that there is only one instance of the logging setup throughout the application.

   Descritption: The Logger class uses the Singleton pattern to ensure that the logging configuration is applied only once, avoiding duplicate logs.
   
   **Strategy Patterns**: The Strategy pattern is used to enable switching between different calculation strategies (e.g., basic and statistical operations) without changing the core calculator logic.

    Description: The Calculator class uses different strategy objects for various operations. This approach makes it easy to add new calculation strategies or modify existing ones.
   
2. Environment Variables
   
3. Logging
   
   The project includes a comprehensive logging system to record detailed application operations, data manipulations, and error messages. This logging system differentiates log messages by severity (INFO, WARNING, ERROR) for effective monitoring and debugging.
   
   
4. Error Handling: LBYL and EAFP
   
   In scenarios where input can be validated before performing an operation (example, checking if a divisor is zero), the LBYL approach is used to prevent errors.

