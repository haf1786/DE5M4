from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Write JSON line entries inside a list with some example books and their availability.

app = FastAPI()

# Fake DB
books = [
    {"id":1, "title":"Harry Potter", "available":True},
    {"id":2, "title":"Eragon", "available":False},
    {"id":3, "title":"The Hobbit", "available":True},
    {"id":4, "title":"The Hobbit 2", "available":True}                          
]

# Home Route
@app.get("/")
def home():
    return {"message":"Haf's Library API"}
            
# Get All Book
@app.get("/books")
def get_book():
    # If done in real life example
    # connect to db
    # run a SQL query
    # get outputs
    # tidy
    # formats
    return books

# Get Available Books
@app.get("/books/available")
def get_available_books():
    available_books = [book for book in books if book["available"]]
    return {"available_books": available_books}

class BookResponse(BaseModel):
    id: int
    title: str
    available: bool

# Check if Specific Book is available
@app.get("/books/{book_id}", response_model=BookResponse)
def check_book_availability(book_id: int):
    book = next((b for b in books if b["id"] == book_id), None)

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book