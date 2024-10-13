import psycopg2
host = 'localhost'
port = 5432
database = 'lectures'
user = 'postgres'
password = 'otari321'

class Book:
   def __init__(self, title, author, release_year, isbn):
      self.title = title
      self.author = author
      self.release_year = release_year
      self.isbn = isbn

connection = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
cursor = connection.cursor()

query = '''create table books(
    id serial primary key,
    title varchar(50),
    author varchar(50),
    release_year int,
    isbn varchar(20) unique
)
'''
cursor.execute(query)
connection.commit()


def book_exists_decorator(func):
    def wrapper(self, *args, **kwargs):
        isbn_input = input('Input Book ISBN: ')
        query = 'SELECT COUNT(*) FROM books WHERE isbn = %s'
        cursor.execute(query, (isbn_input,))
        exist = cursor.fetchone()[0]
        if not exist:
            print('The Book is Not in Database')
            return 
        return func(self, isbn_input, *args, **kwargs)  #
    return wrapper


class Menu:
    def display_menu(self):
        menu = menu = '''1. Add a new Book
2. View All Books
3. Search for a Book
4. Update Book Information
5. Delete a Book
6. Exit'''
        

        print(menu)
        
    def add_book(self):
        title = input('Enter Book Title: ')
        author = input('Enter Book Author: ')
        release_year = int(input('Enter Book\'s release year: '))
        isbn = input('Enter Book isbn: ')
        
        new_book = Book(title, author, release_year, isbn)
        query = '''
            INSERT INTO books (title, author, release_year, isbn)
            VALUES (%s, %s, %s, %s)
        '''
        data = (new_book.title, new_book.author, new_book.release_year, new_book.isbn)
        cursor.execute(query, data)
        connection.commit()
    
    def all_books(self):
        query = 'select * from books'
        cursor.execute(query)
        result = cursor.fetchall()
        
        for i in result:
            print(i)

    @book_exists_decorator
    def search_book(self, isbn_input):
        query = 'select * from books where isbn = %s'
        cursor.execute(query, (isbn_input, ))
        print(cursor.fetchone())

    @book_exists_decorator
    def change_book(self, isbn_input):
        
        valid_columns = {'title', 'author', 'release_year', 'isbn'}
        column = input('Input an Attribute You Want to Change: ')

        if column not in valid_columns:
            print('Not a Valid Attribute')
            return
        
        change_attribute = input('Input a Change: ')

        if column == 'release_year':
            change_attribute = int(change_attribute)

        query = f'update books set {column} = %s where isbn = %s'
        cursor.execute(query, (change_attribute, isbn_input))
        connection.commit()
        print(f'The book\'s {column} has been updated successfully.')

    @book_exists_decorator
    def delete_book(self, isbn_input):
        query = 'delete from books where isbn = %s'
        cursor.execute(query, (isbn_input, ))
        connection.commit()
        print('The Book has Been Deleted')

def main():
    menu = Menu()
    while True:
        menu.display_menu()
        choice = input('Input Your Choice: ')
        if choice == '1':
            menu.add_book()
        elif choice == '2':
            menu.all_books()
        elif choice == '3':
            menu.search_book()
        elif choice == '4':
            menu.change_book()
        elif choice == '5':
            menu.delete_book()
        elif choice == '6':
            print('Exiting the application.')
            cursor.close()
            connection.close()
            break
        else:
            print('Wrong choice')

main()



        


    
    
      





