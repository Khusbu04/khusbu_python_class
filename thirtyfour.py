from queue import Queue
# Create a task queue
task_queue = Queue()
# Add tasks to the queue
tasks = ["Task 1: Clean the room", "Tasks 2: Write Python code", "Tasks 3: Read a book"]
for task in tasks:
    task_queue.put(task)
# Process tasks
print("Processing Tasks:")
while not task_queue.empty():
    print(task_queue.get())