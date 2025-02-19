class Database:
    _instance = None  # Private static variable

    def __new__(cls):
        if cls._instance is None:
            print("Creating new Database connection...")
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

# Testing Singleton
db1 = Database()
db2 = Database()

print(db1 is db2)