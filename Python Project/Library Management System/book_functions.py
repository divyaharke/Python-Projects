import json
from book import Book


#print options
def print_options():
    print("Press the specific button for that action")
    print("1- Create a new book")
    print("2- save book locally")
    print("3- load book from the disk")
    print("4- Find book")
    print("5- issue book")
    print("6- return a book")
    print("7- update a book")
    print("8- show all books")
    print("9- show book")
    print("x/X: Exit")

def input_book_info():
    id= input("ID: ")
    name= input("Name of Book: ")
    description= input("Description: ")
    isbn= input("ISBN: ")
    page_count= int(input("Page Count of a book: "))
    issued= input("Issued: y/Y for True, anything else for False")
    issued= (issued == "y" or issued == "Y")
    author= input("Author name: ")
    year= int(input("Year: "))
    return{
        'id': id,
        'name': name,
        'description': description,
        'isbn': isbn,
        'page_count': page_count,
        'issued': issued,
        'author': author,
        'year': year
    }


#create_book_function
def create_book():
    print("Please enter your book information")
    book_input= input_book_info()
    book= Book(book_input['id'], book_input['name'], book_input['description'], book_input['isbn'], book_input['page_count'],
                 book_input['issued'], book_input['author'], book_input['year'])
    print(book.to_dict())
    return book

#defining save book
def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    try:
        file= open("books.dat", "w")
        file.write(json.dumps(json_books, indent=4))
        print("Books saved successfully")
    except: 
        print("We had an error while saving book")

def load_books():
    try:
        file= open("books.dat", "r")
        loaded_books= json.loads(file.read())
        books = []
        for book in loaded_books:
            new_obj= Book(book['id'], book['name'], book['description'], book['isbn'], book['page_count'],
                 book['issued'], book['author'], book['year'])
            books.append(new_obj)
        print("Successfully loaded books")
        return books
    except:
        print("the file doesn't exists or an error occured during loading")

#find book function
#takes books and id
#if found return the index of book in the books array, if not returning nothing

def find_book(books, id):
    for index, book in enumerate(books):
        if book.id == id:
            return index
        else:
            return "Cannot find the book"
  

#issue book

def issue_book(books):
    id= input("enter the id of the book you want to issue: ")
    index= find_book(books, id)
    if index != None:
        books[index].issued = True
        print("Book successfully issued")
    else:
        print("Could not find the book you are looking for")

#return book

def return_book(books):
    id= input("enter the id of the book you want to return: ")
    index= find_book(books, id)
    if index != None:
        books[index].issued = False
        print("Book successfully returned")
    else:
        print("Could not find the book you are looking for")


#update book
def update_book(books):
    id= input("Enter the ID of book you want to update: ")
    index= find_book(books,id)
    if index != None:
        new_book= create_book()
        old_book= books[index]
        books[index]= new_book
        del old_book
        print("Book successfully updated")
    else:
        print("We could not find your book")

#To view books we write function as show_book and show_all_book
def show_all_book(books):
    for book in books:
        print(book.to_dict())

def show_book(books):
    id= input("Enter the ID of book that you are looking for: ")
    index= find_book(books,id)
    if index != None:
        print(books[index].to_dict())
    else:
        print("we could not find the book you are looking for")