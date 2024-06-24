from fastapi import FastAPI, HTTPException 

from pydantic import BaseModel 

from typing import List, Optional 

# Crear una instancia de FastAPI 

app = FastAPI() 

# Definir el modelo Pydantic para un libro 

class Book(BaseModel): 

    id: int 

    title: str 

    author: str 

    pages: Optional[int] = None 

# Lista de libros inicial 

books = [ 

    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", pages=180), 

    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", pages=281), 

    Book(id=3, title="1984", author="George Orwell", pages=158), 

] 

# Ruta para obtener todos los libros 

@app.get("/books/", response_model=List[Book]) 

async def get_books(): 

    return books 

 # Ruta para obtener un libro por su ID 

@app.get("/books/{book_id}", response_model=Book) 

async def get_book(book_id: int): 

    for book in books: 

        if book.id == book_id: 

            return book 

    raise HTTPException(status_code=404, detail="Libro no encontrado") 

# Ruta para agregar un nuevo libro 

@app.post("/books/", response_model=Book) 

async def create_book(book: Book): 

    books.append(book) 

    return book 

# Ruta para actualizar un libro existente 

@app.put("/books/{book_id}", response_model=Book) 

async def update_book(book_id: int, updated_book: Book): 

    for index, book in enumerate(books): 

        if book.id == book_id: 

            books[index] = updated_book 

            return updated_book 

    raise HTTPException(status_code=404, detail="Libro no encontrado") 

# Ruta para eliminar un libro por su ID 

@app.delete("/books/{book_id}", response_model=Book) 

async def delete_book(book_id: int): 

    for index, book in enumerate(books): 

        if book.id == book_id: 

            deleted_book = books.pop(index) 

            return deleted_book 

    raise HTTPException(status_code=404, detail="Libro no encontrado") 