# API Notes

## What is an API?

## An API, or application programming interface, is a set of rules that enables software  applications to communicate with each other.

## What you built and why it could be useful

## I built an API to manage books from a fake database. It allows the user to perform a number of tasks including (step 1-2) getting available books, (step 3) check if a specific book is available, (step 4) update a title of a book and also (step 5) remove a book.

## Best practise & future scope of work

## I followed a number of best practise steps including documenting my code and I also rewrote code so that it was simpler to understand. I also removed additional code that was no longer required, this included removing unnecessary import steps.

## In future, I plan to add additional functionality to this API to include the ability to add new books and also more information about the books.

## Final MVP is saved in main.py, which can be run using Microsoft Visual Studio Code.

## To run the code, open main.py and select Run Python File.

## In the Python terminal window: enter uvicorn main:app to start the local uvicorn server. Press Ctrl+C to close it. 
## Then make changes and run uvicorn main:app again to reopen it.

## To test functionality, use http://127.0.0.1:8000/docs or http://127.0.0.1:8000 and then navigate to each of the functions.

## Steps completed:

## To check the availability of all books.
## To return only the available books.
## To check the availability of a specific book.
## To update the title of a book. (PUT/PATCH)
## To delete a book (DELETE)
