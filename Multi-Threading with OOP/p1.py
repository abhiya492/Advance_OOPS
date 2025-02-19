import threading
import time

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
        self.__lock = threading.Lock()  # Thread Lock

    def withdraw(self, amount):
        with self.__lock:  # Ensure only one thread modifies the balance
            if self.__balance >= amount:
                print(f"{threading.current_thread().name} withdrawing {amount}...")
                time.sleep(1)  # Simulate delay
                self.__balance -= amount
                print(f"Remaining Balance: {self.__balance}")
            else:
                print(f"{threading.current_thread().name} - Insufficient Funds!")

# Create a shared bank account
account = BankAccount(1000)

# Multiple users trying to withdraw money at the same time
threads = []
for i in range(5):
    t = threading.Thread(target=account.withdraw, args=(200,), name=f"User-{i+1}")
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All transactions completed.")
