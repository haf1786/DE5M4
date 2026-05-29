from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

# Write JSON line entries inside a list with some example books and their availability.

app = FastAPI(title="Simple Book API")

class Book(BaseModel):
    id: int
    title: str
    available: bool

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

# 1 and 2 Get Available Books
@app.get("/books/available")
def get_available_books():
    available_books = [book for book in books if book["available"]]
    return {"available_books": available_books}


# 3 Check if specific book is available
@app.get("/books/{book_id}", response_model=Book)
def check_book_availability(book_id: int):
    book = next((b for b in books if b["id"] == book_id), None)

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book

# 4 Update only the title of a book
@app.patch("/new_books/{book_id}/{title}")
def update_book(book_id: int, title: str):
  for book in books:
    if book["id"] == book_id:
      book["title"] = title
      return {"message": "Book updated", "book": book}
  raise HTTPException(status_code=404, detail="Book not found")

# 5 Remove a book
@app.delete("/books/delete/{book_id}")
def delete_book(book_id: int):
  target_id = book_id -1
  for book in books:
    if book["id"] == book_id:
      del books[target_id]
      return {"message": "Book Deleted", "book": book}
  raise HTTPException(status_code=404, detail="Book not found")