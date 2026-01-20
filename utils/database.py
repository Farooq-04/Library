books = []

def get_all_books():
    return books

def book_exists(name):
    for book in books:
        if book['name'].lower() == name.lower():
            return True
    return False

def insert_book(name, author):
    global books
    if book_exists(name):
        return False
    books.append({
        'name': name,
        'author': author,
        'read': False
    })
    return True

def find_books_by_name(word):
    word = word.lower()
    return [book for book in books if word in book['name'].lower()]

def search_by_author(word):
    word = word.lower()
    return [book for book in books if word in book['author'].lower()]

def search_by_status(status):
    if status == 'read':
        return [book for book in books if book['read']]
    if status == 'unread':
        return [book for book in books if not book['read']]
    return []

def delete_book(book):
    global books
    books.remove(book)
