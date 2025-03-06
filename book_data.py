import json
import os

DATA_FILE = "books.json"

def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_books(books):
    with open(DATA_FILE, "w") as file:
        json.dump(books, file, indent=4)
