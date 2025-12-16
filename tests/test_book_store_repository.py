from lib.book_store_repository import BookStoreRepository
from lib.book_store import BookStore

"""
Given calling book_store_repository#all
Returns list of Book objects
"""

def test_book_store_repository_all_returns_list_book_objects(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookStoreRepository(db_connection)
    books = repository.all()
    assert books[0] == BookStore(1, 'Nineteen Eighty-Four', 'George Orwell')

