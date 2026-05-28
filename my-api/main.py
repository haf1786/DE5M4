from fastapi import FastAPI

# Write JSON line entries inside a list with some example books and their availability.

app = FastAPI()

# Fake DB
books = [
    {"id":1, "title":"Harry Potter", "available":True},
    {"id":2, "title":"Eragon", "available":False},
    {"id":3, "title":"The Hobbit", "available":True}                          
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

# import json

# books = [
#     {"title": "Avengers", "availability": "1 available" },
#     {"title": "Superman", "availability": "4 available" },
#     {"title": "Spiderman", "availability": "2 available" }
# ]

# with open("books.json1", "w", encoding="utf-8") as file:
#     for book in books:
#         json_line = json.dumps(book, ensure_ascii=False)
#         file.write(json_line + "\n")