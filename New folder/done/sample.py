# def divide(a, b):
#   """
#   This function attempts to divide two numbers, but raises a TypeError if b is not a number.
#   """
#   return a / b

# try:
#   # Attempt to divide 10 by "hello" (a string)
#   result = divide(10, "hello")
#   print(result)
# except TypeError as e:
#   # Print the error message
#   print("Error:", e)

  # AttributeError: 'str' object has no attribute 'split'

class MyClass:
    def __init__(self):
        self._private_attribute = 42

obj = MyClass()
print(obj._priate_attribute)  # This is discouraged and may lead to AttributeError
