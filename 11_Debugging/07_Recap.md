# Recap

- The logging module let's you display logging messages

- Log messages create a breadcrumb trail of what a program is doing

- After calling basicConfig() to set up logging, call logging.debug() to create a log message

- When finished, disable the log messages with logging.disable(logging.CRITICAL)

- Don't use the print function for log messages: It's hard to remove them all when you're done debugging

- The five log levels are (DEBUG, INFO, WARNING, ERROR, CRITICAL)

- You can also write the logs to a file using the filename keyword argument to the basicConfig function:
  logging.basicConfig(filename='05_Loggingpy.txt', \
   level=logging.DEBUG, \
   format='%(asctime)s - \
   %(levelname)s - \
   %(message)s')
