#pop() element to remove an item from a list by index and return it
my_list1 = [10, 20, 30, 40, 50]
removed_element1 = my_list1.pop()  # Removes the last element (which is 50)
print("Updated list:",my_list1)  # Output: [10, 20, 30, 40]
my_list2 = [60, 70, 80, 90, 100]
removed_element2 = my_list2.pop(2)
print("Updated list:",removed_element2)  # Output: 80