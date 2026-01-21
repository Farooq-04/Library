from utils import database

MENU = """
a - Add a book
l - List all books
r - Mark book as read
d - Delete a book
s - Search book
u - Update book
p - Sort by price
m - Show min and max price
q - Quit

Enter your choice: """

def menu():
    while True:
        choice = input(MENU).lower()

        if choice == 'a':
            add_book()
        elif choice == 'l':
            show_books()
        elif choice == 'r':
            read_book()
        elif choice == 'd':
            delete_book()
        elif choice == 's':
            search_book()
        elif choice == 'u':
            update_book()
        elif choice == 'p':
            sort_books()
        elif choice == 'm':
            show_min_max()
        elif choice == 'q':
            print("Program closed.")
            break
        else:
            print("Wrong choice.")

def add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    price = input("Enter book price: ")

    if name == "" or author == "" or not price.isdigit():
        print("Invalid input.")
        return

    result = database.insert_book(name, author, int(price))

    if result:
        print("Book added.")
    else:
        print("Book already exists.")

def show_books():
    books = database.get_all_books()
    if not books:
        print("No books found.")
        return
    for book in books:
        status = "Read" if book['read'] else "Not Read"
        print(book['name'], "by", book['author'], "- Price:", book['price'], "-", status)

def read_book():
    word = input("Enter book name or part: ")
    matches = database.find_books_by_name(word)

    if not matches:
        print("No book found.")
        return

    for i, book in enumerate(matches, start=1):
        status = "Read" if book['read'] else "Not Read"
        print(f"{i}. {book['name']} by {book['author']} - {status}")

    choice = input("Enter book number: ")

    if not choice.isdigit():
        print("Invalid choice.")
        return

    choice = int(choice)
    if choice < 1 or choice > len(matches):
        print("Invalid number.")
        return

    matches[choice - 1]['read'] = True
    print("Book marked as read.")

def delete_book():
    word = input("Enter book name or part: ")
    matches = database.find_books_by_name(word)

    if not matches:
        print("No book found.")
        return

    for i, book in enumerate(matches, start=1):
        print(f"{i}. {book['name']} by {book['author']}")

    choice = input("Enter book number: ")

    if not choice.isdigit():
        print("Invalid choice.")
        return

    choice = int(choice)
    if choice < 1 or choice > len(matches):
        print("Invalid number.")
        return

    database.delete_book(matches[choice - 1])
    print("Book deleted.")

def search_book():
    print("""
1 - By book name
2 - By author
3 - By read status
""")

    option = input("Enter option: ")

    if option == '1':
        word = input("Enter book name: ")
        result = database.find_books_by_name(word)
    elif option == '2':
        word = input("Enter author name: ")
        result = database.search_by_author(word)
    elif option == '3':
        status = input("Enter read or unread: ").lower()
        result = database.search_by_status(status)
    else:
        print("Wrong option.")
        return

    if not result:
        print("No book found.")
        return

    for book in result:
        status = "Read" if book['read'] else "Not Read"
        print(book['name'], "by", book['author'], "- Price:", book['price'], "-", status)

def update_book():
    word = input("Enter book name or part: ")
    matches = database.find_books_by_name(word)

    if not matches:
        print("No book found.")
        return

    for i, book in enumerate(matches, start=1):
        status = "Read" if book['read'] else "Not Read"
        print(f"{i}. {book['name']} by {book['author']} - Price:{book['price']} - {status}")

    choice = input("Enter book number: ")

    if not choice.isdigit():
        print("Invalid choice.")
        return

    choice = int(choice)
    if choice < 1 or choice > len(matches):
        print("Invalid number.")
        return

    book = matches[choice - 1]

    print("""
1 - Change book name
2 - Change author name
3 - Change price
4 - Change read status
""")

    option = input("Enter option: ")

    if option == '1':
        new_name = input("Enter new name: ")
        if new_name:
            book['name'] = new_name
            print("Book name updated.")
    elif option == '2':
        new_author = input("Enter new author: ")
        if new_author:
            book['author'] = new_author
            print("Author updated.")
    elif option == '3':
        new_price = input("Enter new price: ")
        if new_price.isdigit():
            book['price'] = int(new_price)
            print("Price updated.")
    elif option == '4':
        book['read'] = not book['read']
        print("Read status updated.")
    else:
        print("Wrong option.")

def sort_books():
    print("""
1 - Price low to high
2 - Price high to low
""")

    option = input("Enter option: ")

    if option == '1':
        database.sort_by_price(True)
        print("Books sorted by price (low to high):")
    elif option == '2':
        database.sort_by_price(False)
        print("Books sorted by price (high to low):")
    else:
        print("Wrong option.")
        return

    for book in database.get_all_books():
        status = "Read" if book['read'] else "Not Read"
        print(book['name'], "by", book['author'], "- Price:", book['price'], "-", status)

def show_min_max():
    min_book = database.get_min_price_book()
    max_book = database.get_max_price_book()

    if not min_book or not max_book:
        print("No books available.")
        return

    print("Lowest price book:", min_book['name'], "-", min_book['price'])
    print("Highest price book:", max_book['name'], "-", max_book['price'])

menu()
