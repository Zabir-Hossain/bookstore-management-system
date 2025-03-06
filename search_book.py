from book_data import load_books

def search_book():
    books = load_books()
    
    print("\n--- Search for a Book ---")
    search_term = input("Enter the title, author, or ISBN: ").lower()
    
    results = [
        book for book in books
        if (search_term in book['title'].lower() or
            search_term in book['author'].lower() or
            search_term == book['isbn'])
    ]
    
    if not results:
        print("No matching books found.")
        return
    
    print("\n--- Search Results ---")
    for book in results:
        print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
