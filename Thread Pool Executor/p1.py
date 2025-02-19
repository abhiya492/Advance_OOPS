import concurrent.futures
import time

def process_task(task_id):
    print(f"Task {task_id} started...")
    time.sleep(2)  # Simulate work
    print(f"Task {task_id} completed.")

# Using ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    tasks = [executor.submit(process_task, i) for i in range(5)]

    for task in concurrent.futures.as_completed(tasks):
        task.result()  # Wait for completion
