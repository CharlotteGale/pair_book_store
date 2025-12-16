# Book Store Model and Repository Classes Design Recipe


## 1. Design and create the Table



```
# EXAMPLE

Table: books

Columns:
id | title | author_name
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- EXAMPLE
-- (file: spec/seeds_book_store.sql)

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_name VARCHAR(255)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO books (title, author_name) VALUES ('Nineteen Eighty-Four', 'George Orwell');
INSERT INTO books (title, author_name) VALUES ('Mrs Dalloway', 'Virginia Woolf');
INSERT INTO books (title, author_name) VALUES ('Emma', 'Jane Austen');
INSERT INTO books (title, author_name) VALUES ('Dracula', 'Bram Stoker');
INSERT INTO books (title, author_name) VALUES ('The Age of Innocence', 'Edith Wharton');
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 book_store < seeds_books.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/book_store.py)
class BookStore


# Repository class
# (in lib/book_store_repository.py)
class BookStoreRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: book_store

# Model class
# (in lib/book_store.py)

class BookStore:
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name

```

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: book_store

# Repository class
# (in lib/book_store_repository.py)

class BookStoreRepository():
    def __init__(self):
        # Connect to DB
        pass

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, title, author_name FROM book_store;

        # Returns an array of Book objects.


```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all students

repo = BookStoreRepository()

book_store = repo.all()

len(book_store) # =>  5

book_store[0].id # =>  1
book_store[0].title # =>  'Nineteen Eighty-Four' 
book_store[0].author_name # =>  'George Orwell'

book_store[3].id # =>  4
book_store[3].name # =>  'Dracula'
book_store[3].cohort_name # =>  'Bram Stoker'

```

Encode this example as a test.
