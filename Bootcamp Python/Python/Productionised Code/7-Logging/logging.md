
# Logging

Why is logging important? **Python Logging** is a way to track and record elements of your Python script or program. It aids us in problem solving- when something goes wrong in our script, logging allows us to **inspect and detect the cause of the problem**. Logging simply enables us to leave hints as to what our program is doing, so that when something unexpected happens, it's easier to detect why.

Python has a built-in package `logging` for logging events for Python applications, which we will look at.

## Log Levels
There are five standard logging levels based on the severity of the events they track. These are given below along with their corresponding numeric values in brackets:
- **DEBUG** (10): Detailed information. Useful for debugging the code 
- **INFO**  (20): Information messages to show that everything is working as expected
- **WARNING** (30): Warning messages indicate that something unexpected has happened albeit without any interruption to the program execution
- **ERROR** (40): Error messages are displayed when the program is unable to perform some function
- **CRITICAL** (50): For more serious errors - the program may not be able to continue running properly

## Advantages of Logging over Diagnostic Print Messages
- Messages can be categorised and filtered depending on their level of severity
- Logs are highly customisable and can be formatted to include timestamps, line numbers etc. to provide more descriptive information
- It is easy to turn logging on/off, this is particularly useful when your package is imported into other Python packages
- You can output the log messages to a file as well as have them displayed in the terminal

## Filtering the Log Messages
- In a production execution environment, we would choose to set the logging level to `logging.INFO` or `logging.WARNING`, depending on the expected volume of messages and how long we expected the program to stay running. 
- In a development ('debugging') execution environment, we would choose to set the logging level to `logging.DEBUG`, so that we can see all the relevant messages. 

## Using the `logging` module
When you import the `logging` module, it provides methods to log messages at each of the levels specified above. In order to access each of these methods, you use the `logging.<log level>('message to output')` syntax.  As the author of a script, you can then call these methods at appropriate points in your code. 

```Python
"""A script to demonstarte the logging module"""
import logging

logging.debug("This is a debug message") # Detailed information, typically useful for debugging purposes
logging.info("This is a info message") # General information about the progress or state of the program
logging.warning("This is a warning message") # Indication of a potential problem or a non-fatal issue that deserves attention
logging.error("This is a error message") # A more severe problem that prevents the program from executing a particular function or task
logging.critical("This is a critical message") # A critical error that may cause the program to terminate or result in system instability

```
After executing the above script, you will see only the final 3 messages are displayed. That's because the logging module automatically sets the default logging level to `WARNING`. This means that by default, only messages of `WARNING` level and higher (i.e., `ERROR` and `CRITICAL`) will be processed and outputted, while messages of lower severity (`DEBUG` and `INFO`) will be ignored. 

### Changing the Log Level
However, you can configure the logging level to a lower level, such as `DEBUG`, to enable logging of all messages, including `DEBUG` level messages. Logging provides a `basicConfig` method to do this. 
For example:

```Python
"""A script to demonstarte the logging module"""
import logging

logging.basicConfig(level='DEBUG')
logging.debug("This is a debug message") # Detailed information, typically useful for debugging purposes
logging.info("This is a info message") # General information about the progress or state of the program
logging.warning("This is a warning message") # Indication of a potential problem or a non-fatal issue that deserves attention
logging.error("This is a error message") # A more severe problem that prevents the program from executing a particular function or task
logging.critical("This is a critical message") # A critical error that may cause the program to terminate or result in system instability

```
(Note: this `basicConfig` method can only be called once)

### Changing the Location the Messages are Outputted to
So far, each log message has been outputted to the console as this is the default location, but you can specify a different location. For example, we can output the log messages to a file: 
```Python
"""A script to demonstarte the logging module"""
import logging

logging.basicConfig(level='ERROR', filename='tutorial.log', filemode='w')
logging.debug("This is a debug message") # Detailed information, typically useful for debugging purposes
logging.info("This is a info message") # General information about the progress or state of the program
logging.warning("This is a warning message") # Indication of a potential problem or a non-fatal issue that deserves attention
logging.error("This is a error message") # A more severe problem that prevents the program from executing a particular function or task
logging.critical("This is a critical message") # A critical error

```
The log messages will now be written to a file named `tutorial.log` instead of the console. Also, the filemode is set to `w`, which means the log file is opened in write mode each time script is executed. 
Note: The default configuration for filemode is `a`, which is append.

### Formatting Each Message
>  Nowadays, there are a few different ways we can format a string in Python, found [here](https://dev.to/izabelakowal/what-is-the-best-string-formatting-technique-for-logging-in-python-d1d). <br>
Logging was a module created when the only string formatting option was using '%', so when it comes to formatting our logging messages, we have to use this formatting style. 

In all of our log messages so far we have seen the message we have inputted in the logging function, as well as some extra information, namely, the level of the log and `root` which is the default name for the log. 

This is the default format for every log message. However, we can customise this format within our `basicConfig` call. Within this customised format, we can include fundamental attributes already present in the LogRecord. A list of these attributes and how to include them in our format can be found [here](https://docs.python.org/3/library/logging.html#logrecord-attributes)

A `LogRecord` encapsulates all the information needed to define the status of an event being logged. It contains details like the log message, log level, logger name, timestamp, and other contextual information. 

```Python
"""A script to demonstarte the logging module"""
import logging

logging.basicConfig(level='ERROR',format='%(levelname)s - %(asctime)s - %(message)s - %(module)s', filename='tutorial.log', filemode = 'w')
logging.debug("This is a debug message") # Detailed information, typically useful for debugging purposes
logging.info("This is a info message") # General information about the progress or state of the program
logging.warning("This is a warning message") # Indication of a potential problem or a non-fatal issue that deserves attention
logging.error("This is a error message") # A more severe problem that prevents the program from executing a particular function or task
logging.critical("This is a critical message") # A critical error

```


### Concept Check
Amend the above script so that:
- The log messages are outputted to a file in the root of the Production Python directory we have made. 
- Each log message is formatted so that the module name from which the log message comes from is included as the first part of the string. 


## Custom Loggers
So far, we have used the default logger, (named `root`) to produce log messages. In practice however relying solely on the default logger can introduce several challenges: 

- **Namespace Collisions**: When multiple modules within an application use the root logger, there's a risk of having log messages from different modules logged under the same name. This can lead to confusion about the origin of these messages. 

- **Lack of Control**: When relying solely on the root logger, controlling the log level for different aspects of the application becomes difficult. This lack of control can result in either excessive logging, flooding logs with unnecessary information, or insufficient logging, omitting critical details.

- **Cannot Work With Multiple Handlers**: It will not work simultaneously for multiple handlers at a time, i.e., you can’t use both console or file simultaneously for logging. 

Instead, it's advisable to create a separate logger for each module within your application. 


### Steps to create a simple custom logger: 
#### 1. Create a logger
When creating a logger, we need two methods – `getLogger()` and `setLevel()`.
`getLogger()` takes a single argument, which is the name of the custom logger - recommendation is to set it to `__name__`. When executed, this method creates a custom logger with the specified name. `setLevel()` is responsible for setting logger's lowest level that custom logger generates.

```Python 
"""A script to demonstarte the logging module"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


logger.debug("This is a debug message")
logger.info("This is a info message") 
logger.warning("This is a warning message") 
logger.error("This is a error message") 
logger.critical("This is a critical message") 

```

Here, `getLogger()` creates and references a custom logger which we have set the name to be `__name__`. `setLevel()` sets the **lowest** level of messages generated by our logger to `DEBUG`.

If you don't specify a handler or file type, the messages will be logged to the console and just output the log message. 

#### 2: Create a Handler and Assign it to the Cutom Logger 
Once the logger is created, you have to assign the necessary handler. There are different [handlers](https://docs.python.org/3/library/logging.handlers.html) provided in the `logging` package. We will create a `FileHandler`

```Python 
"""A script to demonstarte the logging module"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

custom_fileHandler = logging.FileHandler('custom_loging.log')
custom_fileHandler.setLevel(logging.INFO)

logger.addHandler(custom_fileHandler)

logger.debug("This is a debug message")
logger.info("This is a info message") 
logger.warning("This is a warning message") 
logger.error("This is a error message") 
logger.critical("This is a critical message") 
```
This will now output the log messages to `custom_loging.log` - but sets the severity level of this handler to be `INFO`. 

#### 3: Create a Formatter
You can create a formatter object and specify the formatting to the output, this logger generates. You then have to add this formatter object to the handler object using the `setFormatter()` method. (Note: The formatter object has to be added to the handler object before the handler object is added to the custom logger)


```Python 
"""A script to demonstarte the logging module"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

custom_fileHandler = logging.FileHandler('custom_loging.log')
custom_fileHandler.setLevel(logging.INFO)

custom_fileFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
custom_fileHandler.setFormatter(exampleFormatter)

logger.addHandler(custom_fileHandler)

logger.debug("This is a debug message")
logger.info("This is a info message") 
logger.warning("This is a warning message") 
logger.error("This is a error message") 
logger.critical("This is a critical message") 
```


#### Concept Check
We have added a `FileHandler` to our above custom logger, however a great thing about using custom loggers, is that you can add multiple handlers, which mean the log messages can be outputetd in different places, and each handler can have it's own customisation. With this in mind, amend the above code so that:
- The log messages are also outputted to the console. (Note: use a `StreamHandler`). 
- Only log messages of level `INFO` and above are outputted to the console, whilst ensuring log messages of level `WARNING` and above are outputted to the file we have specified. 
- The message outputted to the console should be formatted to include the line number in which the log message occurs in the Python file. (Note: Refer to the [LogRecord attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes)). 







