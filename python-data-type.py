# #Create a list
# frutes = ['
# apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
# print(frutes)
# print(f"Innitial frutes: {frutes}")
# #Accessing elements in a list
# print(f"First frute:{frutes[0]}")
# print(f"Last frute:{frutes[-1]}")
# modiqfying elements in a list
# frutes[0] = 'avocado'
# print(f"Modified frutes: {frutes}")
# #Adding elements to a list
# frutes.append('grape')
# print(f"After adding frutes: {frutes}")
# frutes.insert(2, 'pear')
# print(f"After inserting frutes: {frutes}")
# #Removing elements from a list
# frutes.remove('banana')
# print(f"After removing frutes: {frutes}")
# #Removing the last element
# last_frute = frutes.pop()
# print(f"After popping last frute: {frutes}, popped frute: {last_frute}")
# del frutes[1]
# print(f"After deleting frute at index 1: {frutes}")

# Sorting a list
# frutes.sort()
# print(f"Sorted frutes: {frutes}")
# #Reversing a list
# frutes.reverse()
# print(f"Reversed frutes: {frutes}")


#List slicing (getting a sub list )
# numbers = [30, 10, 20, 50, 40]
# # subsert = numbers[3:4]  # Get elements from index 1 to 3]
# # print(f"Subset of numbers: {subsert}")
# #List comprehension
# squares_numbers = [x**2 for x in range(20)]
# print(f"Squares of numbers: {squares_numbers}")
# # Filtering even numbers using list comprehension
# even_numbers = [x for x in range(20) if x % 2 == 0]
# print(f"Even numbers: {even_numbers}")
# # Filtering odd numbers using list comprehension
# odd_numbers = [x for x in range(20) if x % 2 != 0]
# print(f"Odd numbers: {odd_numbers}")
#nested lists
# nested_list = [
#             [1, 2, 3], 
#             [4, 5, 6], 
#             [7, 8, 9]
#                ]
# print(f"Nested list: {nested_list}")
# print(f"First element of first sublist: {nested_list[0][0]}")
# print(f"Last element of last sublist: {nested_list[-1][-1]}")


#Create a dictionary
# student = {
#     'name': 'John Doe',
#     'age': 20,
#     'courses': ['Math', 'Science', 'History']
# }
# print(f"Initial student dictionary: {student}")
# # Accessing value by key
# print(f"Student's name: {student['name']}")
# print(f"Student's age: {student.get('age')}")
# print(f"Student's courses: {student['courses']}")
# # Modifying values in a dictionary
# student['age'] = 21
# print(f"Modified student dictionary: {student}")
# # Adding new key-value pairs
# student['grade'] = 'A'
# print(f"After adding grade: {student}")
# # Removing 'Science' from courses list
# student['courses'].remove('Science')
# print(f"After removing Science from courses: {student}")

    # my_list = [1, 2, 3]
    # my_tuple = (4, 5, 6)
    # my_set = {7, 8, 9}
    # my_dict = {"a": 10, "b": 11}
    
    # for item in my_list: pass
    # for item in my_tuple: pass
    # for item in my_set: pass
    # for key in my_dict: pass # Iterates keys
    # for value in my_dict.values(): pass
    # for key, value in my_dict.items(): pass
    # print(5 in my_list)
    # print("c" in my_set)
    # print("a" in my_dict) # Checks if 'a' is a key
    # print(len(my_list))
    # print(len(my_tuple))
    # print(len(my_set))
    # print(len(my_dict))

# my_dict = {"name": "Alice", "age": 30}
# print(my_dict["name"]) # Output: Alice
# print(my_dict.get("city", "Unknown")) 
# Iterating over a list
