books = []

def get_all_books():
    return books

def book_exists(name):
    for book in books:
        if book['name'].lower() == name.lower():
            return True
    return False

def insert_book(name, author, price):
    global books
    if book_exists(name):
        return False
    books.append({
        'name': name,
        'author': author,
        'price': price,
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

def sort_by_price(low_to_high=True):
    global books
    books.sort(key=lambda b: b['price'], reverse=not low_to_high)

def get_min_price_book():
    if not books:
        return None
    return min(books, key=lambda b: b['price'])

def get_max_price_book():
    if not books:
        return None
    return max(books, key=lambda b: b['price'])
