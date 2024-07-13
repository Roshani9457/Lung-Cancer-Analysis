import os
import pandas as pd 
class DataCleaningError(Exception):
    #Defines a custom exception class named DataCleaningError that inherits from 
    # Python's built-in Exception class. This means DataCleaningError is a type of 
    # Exception and can be raised like any other exception in Python.
    def __init__(self, message="Error during data cleaning"):
        #initializer (constructor) method for the DataCleaningError class.
        self.message = message
        # instance variable message with a default value of "Error during data cleaning".
        # This message can be customized when an instance of DataCleaningError is created.
        super().__init__(self.message)
        #Calls the initializer of the parent class (Exception) with the message attribute. 
        # This sets the error message for the exception.