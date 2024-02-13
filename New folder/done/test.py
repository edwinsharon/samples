# file1 = open("Employees.txt", "w") 
# lst = [] 
# for i in range(3): 
# 	name = input("Enter the name of the employee: ") 
# 	lst.append(name + '\n') 
	
# file1.writelines(lst) 
# file1.close() 
# print("Data is written into the file.") 
# file1=open("Employees.txt","r")
# a=file1.readlines(5)
# print(a) 
# Python program to
# demonstrate reading files
# using for loop

# L = ["Geeks", "for\n", "Geeks\n"]

# # Writing to file
# file1 = open('myfile.txt', 'w')
# file1.writelines(L)
# file1.close()

# Opening file
# file1 = open('myfile.txt', 'r')
# count = 0

# # Using for loop
# print("Using for loop")
# for line in file1:
# 	count += 1
# 	print("Line{}: {}".format(count, line.strip()))

# Closing files
# file1.close()


# name = "Ram"
# age = 22
# message = "My name is {0} and I am {1} years \
# 					old. {1} is my favorite \
# 					number.".format(name, age)
# print(message)



# a=5
# b=2
# try:
# 		c = ((a+b) / (a-b))
# 		print(c)
# except ZeroDivisionError:
# 		print ("a/b result in 0")
# else:
# 		print (c)


# try: 
# 	pass
# except NameError:
# 	print ("An exception")
# 	raise TypeError("hello")

# a="hello"
# b=0
# c=a/b

# Attempt to import a module from a non-standard location
# import my_custom_module  # Assuming this module is not in a standard library path

# # Handle potential ImportError in a try-except block
# try:
#   print(my_custom_module.add(5, 3))
# except ImportError as e:
#   print("Error:", e)
#   print("This error likely occurred because 'my_custom_module' is not in a standard location.")
#   print("Consider adding its directory to your Python path or installing it using pip.")


def sum():
    print("hai")
