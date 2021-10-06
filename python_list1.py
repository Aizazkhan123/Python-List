#!/usr/bin/env python
# coding: utf-8

# # Python List:
# A list is a container which holds comma-separated values (items or elements) between square brackets where items or elements need not all have the same type.

# In[3]:


my_list1 = [5, 12, 13, 14] # the list contains all integer values
print(my_list1)


# # list contains all string:

# In[5]:


my_list2 = ['red', 'blue', 'black', 'white'] # the list contains all string
print(my_list2)



# In[6]:


my_list3 = ['red', 12, 112.12] # the list contains a string, an integer and a float values
print(my_list3)


# # Use + operator to create a new list that is a concatenation of two lists and use * operator to repeat a list. See the following statements.

# In[7]:


color_list1 = ["White", "Yellow"]
color_list2 = ["Red", "Blue"]
color_list3 = ["Green", "Black"]
color_list = color_list1 + color_list2 + color_list3
print(color_list)
number = [1,2,3]
print(number[0]*4)
print(number*4)


# # List indices

# In[10]:


color_list=["Red", "Blue", "Green", "Black"] # The list have four elementsindices start at 0 and end at 3
color_list[0] # Return the First Element
print(color_list[0],color_list[3]) # Print First and Last Elements
color_list[-1] # Return Last Element
    


# # Add an item to the end of the list

# In[11]:


color_list=["Red", "Blue", "Green", "Black"]
print(color_list)

color_list.append("Yellow")
print(color_list)


# # Insert an item at a given position

# In[12]:


color_list=["Red", "Blue", "Green", "Black"]
print(color_list)
color_list.insert(2, "White") #Insert an item at third position
print(color_list)


# # Modify an element by using the index of the element

# In[14]:


color_list=["Red", "Blue", "Green", "Black"]
print(color_list)
color_list[2]="Yellow"  #Change the third color
print(color_list)


# # Remove an item from the list

# In[15]:


color_list=["Red", "Blue", "Green", "Black"]
print(color_list)
color_list.remove("Black")
print(color_list)


# # Remove all items from the list

# In[16]:


color_list=["Red", "Blue", "Green", "Black"]
print(color_list)
color_list.clear()
print(color_list)


# # Slicing list:
# This refers to the items of a list starting at index startIndex and stopping just before index endIndex. The default values for list are 0 (startIndex) and the end (endIndex) of the list. If you omit both indices, the slice makes a copy of the original list.

# In[18]:


color_list=["Red", "Blue", "Green", "Black"] # The list have four elements indices start at 0 and end at 3
print(color_list[0:2]) # cut first two items
['Red', 'Blue']


# In[19]:


color_list=["Red", "Blue", "Green", "Black"] # The list have four elements indices start at 0 and end at 3
print(color_list[1:2])

print(color_list[1:-2])


# # Remove the item at the given position in the list, and return it

# In[20]:


color_list=["Red", "Blue", "Green", "Black"]
print(color_list)

color_list.pop(2) # Remove second item and return it
print(color_list)
['Red', 'Blue', 'Black']


# # Sort the items of the list in place

# In[21]:


color_list=["Red", "Blue", "Green", "Black"]
print(color_list)

color_list.sort(key=None, reverse=False)
print(color_list)


# In[ ]:




