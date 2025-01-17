from collections import deque
# Create a deque for task management
task_manager = deque()
# Function to add a task at the end
def add_task(task):
    task_manager.append(task)
    print(f"Task '{task}' added.")
# Function to remove a task from the front
def remove_task():
    if task_manager:
        task = task_manager.popleft()
        print(f"Task '{task}' removed.")
    else:
        print("No tasks to remove.")
# Function to rotate tasks
def rotate_tasks(steps=1):
    task_manager.rotate(steps)
    print(f"Tasks rotated by {steps} steps.")
# Example usage
add_task("Task 1")
add_task("Task 2")
add_task("Task 3")
print("Current Tasks:", task_manager)
remove_task()
print("Current Tasks:", task_manager)
rotate_tasks(1)
print("Current Tasks:", task_manager)

# Q. Understanding collections Module
   #Assignments
     #Task Management with deque: Create a task manager using deque to:
          #Add tasks at the end of the list.
          #Remove tasks from the front of the list.
          #Rotate tasks if a task gets postponed.
  

from collections import Counter
# Sample paragraph
paragraph = "This is a sample paragraph."
# Function to count word frequency and display top 3 most common words
def word_frequency_counter(text):
    words = text.split()
    counter = Counter(words)
    most_common = counter.most_common(3)
    return most_common
# Example usage
top_words = word_frequency_counter(paragraph)
print("Top 3 most common words:", top_words)

# Q. Word Frequency Counter with Counter: Given a paragraph, count the frequency of each word using Counter and display the top 3 most common words.


from collections import defaultdict
# Create a defaultdict for inventory management
inventory = defaultdict(list)
# Function to add a product to an inventory category
def add_product(category, product):
    inventory[category].append(product)
    print(f"Product '{product}' added to category '{category}'.")
# Example usage
add_product("Electronics", "Laptop")
add_product("Electronics", "Smartphone")
add_product("Groceries", "Apple")
print("Current Inventory:", dict(inventory))

# Q. Inventory Management with defaultdict: Create an inventory tracker where each product is stored under its category. Use defaultdict for auto-creating empty categories.


