# ==============================
# TASK MANAGEMENT SYSTEM
# STACK + QUEUE IMPLEMENTATION
# ==============================

from collections import deque

# Queue for task scheduling (FIFO)
task_queue = deque()

# Stack for undo operations (LIFO)
undo_stack = []


# Add a task to the queue
def add_task(task):
    task_queue.append(task)
    print(f"Task added: {task}")


# Process the first task in the queue
def process_task():
    if task_queue:
        task = task_queue.popleft()
        undo_stack.append(task)
        print(f"Processed task: {task}")
    else:
        print("No tasks to process")


# ==============================
# Main Program
# ==============================

add_task("Complete Assignment")
add_task("Attend Lecture")
add_task("Submit Project")

print("\nProcessing Tasks:")

process_task()
process_task()
process_task()

print("\nRemaining Tasks:", list(task_queue))
print("Undo Stack:", undo_stack)