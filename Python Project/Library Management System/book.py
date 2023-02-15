class Book:
    def __init__(self,id, name, description, isbn, page_count, issued, author, year):
        self.id= id
        self.name= name
        self.description= description
        self.isbn= isbn
        self.page_count= page_count
        self.issued= issued
        self.author= author
        self.year= year
    
    #to_dict method
    def to_dict(self):
        dictionary= {
            "id":self.id,
            "name": self.name,
            "description": self.description,
            "isbn": self.isbn,
            "page_count": self.page_count,
            "issued": self.issued,
            "author": self.author,
            "year": self.year
        }
        return dictionary

#book= Book(12, "atomic habits","buid long habits","213-52-325-23",234, True, "James Clear", 2022)

#print(book.to_dict())