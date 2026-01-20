from utils import database

MENU = """
a - Add a book
l - List all books
r - Mark book as read
d - Delete a book
s - Search book
u - Update book
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
        elif choice == 'q':
            print("Program closed.")
            break
        else:
            print("Wrong choice.")

def add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")

    if name == "" or author == "":
        print("Invalid input.")
        return

    result = database.insert_book(name, author)

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
        print(book['name'], "by", book['author'], "-", status)

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

    choice = input("Enter book number to delete: ")

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
        print(book['name'], "by", book['author'], "-", status)

def update_book():
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

    book = matches[choice - 1]

    print("""
1 - Change book name
2 - Change author name
3 - Change read status
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
        book['read'] = not book['read']
        print("Read status updated.")
    else:
        print("Wrong option.")

menu()
