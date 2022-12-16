#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a program to find all pairs of an integer array whose sum is equal to a given number?

# Define the target sum
target_sum = 10

# Define the array of integers
numbers = [2, 7, 4, 1, 5, 3, 9]

for i in range(len(numbers)):
  for j in range(i+1, len(numbers)):
    if numbers[i] + numbers[j] == target_sum:
      print("Pair found: ", (numbers[i], numbers[j]))


# In[3]:


# Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
# Define the array
numbers = [1, 2, 3, 4, 5, 6]

numbers.reverse()

print(numbers)


# In[4]:


#Write a program to check if two strings are a rotation of each other
# Define the two strings to check
string1 = "hello"
string2 = "lohel"


if len(string1) != len(string2):
  print("The strings are not a rotation of each other")
else:

  concat_string = string1 + string1

  
  if string2 in concat_string:
    print("The strings are a rotation of each other")
  else:
    print("The strings are not a rotation of each other")


# In[5]:


#Write a program to print the first non-repeated character from a string
# Define the string
string = "hello"


for char in string:
  if string.count(char) == 1:
    print("The first non-repeated character is: ", char)
    break


# In[6]:


def hanoi(n, source, helper, target):
  # If there is only one disk, move it from the source peg to the target peg
  if n == 1:
    print("Move disk 1 from peg", source, "to peg", target)
    return

  
  hanoi(n - 1, source, target, helper)


  print("Move disk", n, "from peg", source, "to peg", target)

  
  hanoi(n - 1, helper, source, target)

# Define the number of disks
n = 3

# Solve the Tower of Hanoi puzzle with n disks
hanoi(n, 1, 2, 3)


# In[7]:


#Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression
def postfix_to_prefix(expression):
  stack = []
 
  for char in expression:
    
    if char.isnumeric():
      stack.append(char)
   
    else:
      operand1 = stack.pop()
      operand2 = stack.pop()
      stack.append(char + operand2 + operand1)
  
  return stack[-1]

# Test the postfix_to_prefix function
print(postfix_to_prefix("23+"))  
print(postfix_to_prefix("23*"))  
print(postfix_to_prefix("23+5*"))  


# In[8]:


#Write a program to convert prefix expression to infix expression.
def prefix_to_infix(expression):
  stack = []
  
  for char in reversed(expression):
    
    if char.isnumeric():
      stack.append(char)
    
    else:
      operand1 = stack.pop()
      operand2 = stack.pop()
      stack.append("(" + operand1 + char + operand2 + ")")
  
  return stack[-1]

# Test the prefix_to_infix function
print(prefix_to_infix("+23"))  
print(prefix_to_infix("*23"))  
print(prefix_to_infix("*+235")) 


# In[9]:


#Write a program to check if all the brackets are closed in a given code snippet
def check_brackets(code):
  stack = []
  # Loop through each character in the code
  for char in code:
   
    if char in ("(", "[", "{"):
      stack.append(char)
    
    elif char in (")", "]", "}"):
      if not stack:
        return False
      if char == ")" and stack[-1] != "(":
        return False
      if char == "]" and stack[-1] != "[":
        return False
      if char == "}" and stack[-1] != "{":
        return False
      stack.pop()
  return not stack

# Test the check_brackets function
print(check_brackets("int main() { return 0; }")) 
print(check_brackets("int main() { return 0;")) print(check_brackets("int main() { return 0; }]"))  


# In[10]:


#Write a program to reverse a stack.
def reverse_stack(stack):
  # Create a new empty stack
  new_stack = []
  
  for i in range(len(stack)-1, -1, -1):
    
    new_stack.append(stack.pop())
  
  return new_stack

# Test the reverse_stack function
stack = [1, 2, 3, 4, 5]
print(reverse_stack(stack))  


# In[15]:


#Write a program to find the smallest number using a stack
def find_smallest(stack):
  
  smallest = stack[0]
 
  for num in stack:
    
    if num < smallest:
      smallest = num   
  return smallest

# Test the find_smallest function
stack = [5, 3, 7, 2, 4]
print(find_smallest(stack))  


# In[ ]:





# In[ ]:




