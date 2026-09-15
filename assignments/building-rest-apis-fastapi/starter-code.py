from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Book Catalog API")


class Book(BaseModel):
    title: str
    author: str
    year: int


books = [
    {"id": 1, "title": "The Hobbit", "author": "J. R. R. Tolkien", "year": 1937},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
]


@app.get("/health")
def health_check():
    """Return the current API status."""
    return {"status": "ok"}


@app.get("/books")
def list_books():
    # Return all books in the in-memory catalog.
    pass


@app.post("/books", status_code=201)
def create_book(book: Book):
    # Add the book to the catalog with a new unique integer ID.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # Return the requested book or raise HTTPException with status 404.
    pass
