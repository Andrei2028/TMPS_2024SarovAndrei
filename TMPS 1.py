# Factory Method Pattern
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class MemberUser(User):
    def __init__(self, name, user_id, borrowed_books=None):
        super().__init__(name, user_id)
        self.borrowed_books = borrowed_books if borrowed_books else []

class AdminUser(User):
    def __init__(self, name, user_id, permissions=None):
        super().__init__(name, user_id)
        self.permissions = permissions if permissions else []

class UserFactory:
    @staticmethod
    def create_user(user_type, name, user_id):
        if user_type == "member":
            return MemberUser(name, user_id)
        elif user_type == "admin":
            return AdminUser(name, user_id)

# Singleton Pattern
class LibraryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LibraryManager, cls).__new__(cls)
            cls._instance.books = []
            cls._instance.users = []
        return cls._instance

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

# Builder Pattern
class Book:
    def __init__(self):
        self.title = None
        self.author = None
        self.genre = None
        self.isbn = None

    def __str__(self):
        return f"{self.title} by {self.author} (Genre: {self.genre}, ISBN: {self.isbn})"

class BookBuilder:
    def __init__(self):
        self.book = Book()

    def with_title(self, title):
        self.book.title = title
        return self

    def with_author(self, author):
        self.book.author = author
        return self

    def with_genre(self, genre):
        self.book.genre = genre
        return self

    def with_isbn(self, isbn):
        self.book.isbn = isbn
        return self

    def build(self):
        return self.book

# Usage
# Factory Method - Creating Users
user1 = UserFactory.create_user("member", "Alice", "M001")
user2 = UserFactory.create_user("admin", "Bob", "A001")

# Singleton - Library Manager
manager = LibraryManager()
manager.add_user(user1)
manager.add_user(user2)

# Builder - Creating Books
book_builder = BookBuilder()
book1 = book_builder.with_title("Python Programming").with_author("John Doe").with_genre("Programming").with_isbn("123456789").build()
book2 = book_builder.with_title("Data Science Essentials").with_author("Jane Smith").with_genre("Data Science").with_isbn("987654321").build()

manager.add_book(book1)
manager.add_book(book2)

print("Library Users:")
for user in manager.users:
    print(f"{user.name} ({user.user_id})")

print("\nLibrary Books:")
for book in manager.books:
    print(book)
