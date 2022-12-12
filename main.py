from fastapi import FastAPI, APIRouter, Body, Path, HTTPException, Query
from books_data import DATA
from schemas import Book
import utils


app = FastAPI(title='Books API')
book_router = APIRouter(prefix="/book")

BOOKS_DATA = [Book(**book) for book in DATA]

@book_router.get("/")
async def get_book(max_results: int = Query(default=None)):
    return BOOKS_DATA[:max_results]

@book_router.post("/create", status_code=200)
async def create_book(book: Book = Body()):
    params = book.dict()
    params["id"] = len(BOOKS_DATA) + 1
    BOOKS_DATA.append(Book(**params))

@book_router.put("/update/{book_id}",status_code=200)
async def update_book(book: Book = Body(), book_id: int = Path()):
    global BOOKS_DATA
    q_result = utils.find_book("id", book_id, BOOKS_DATA)
    if not q_result:
        raise HTTPException(status_code=404, detail=f"book with id {book_id} not found")
    params = book.dict()
    params["id"] = book_id
    BOOKS_DATA[q_result[0]] = Book(**params)

@book_router.delete("/delete/{book_id}")
async def delete_book(book_id: int = Path()):
    global BOOKS_DATA
    q_result = utils.find_book("id", book_id, BOOKS_DATA)
    if not q_result:
        raise HTTPException(status_code=404, detail=f"book with id {book_id} not found")
    BOOKS_DATA.remove(q_result[1])
    books_params = [book.dict() for book in BOOKS_DATA]
    for i, book_params in enumerate(books_params):
        book_params["id"] = i + 1
    BOOKS_DATA = [Book(**param) for param in books_params]


app.include_router(book_router)


