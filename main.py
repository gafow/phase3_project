from models import Book, Author
from database import SessionLocal, engine
from sqlalchemy.orm import Session

# Create the tables in the database
def init_db():
    from models import Base
    Base.metadata.create_all(bind=engine)

# Add a book
def add_book(title: str, author_name: str, db: Session):
    author = db.query(Author).filter(Author.name == author_name).first()
    if not author:
        author = Author(name=author_name)
        db.add(author)
        db.commit()
        db.refresh(author)
    
    new_book = Book(title=title, author_id=author.id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# Add an author
def add_author(name: str, db: Session):
    new_author = Author(name=name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

# Update book
def update_book(book_id: int, new_title: str, db: Session):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        book.title = new_title
        db.commit()
        db.refresh(book)
    return book

# Delete book
def delete_book(book_id: int, db: Session):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book

# Retrieve a list of all books
def list_books(db: Session):
    return db.query(Book).all()

# Retrieve author of a specific book
def get_author_by_book(book_id: int, db: Session):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        return book.author
    return None
