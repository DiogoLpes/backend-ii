import strawberry
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@db:5432/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class BookModel(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    published_year = Column(Integer)


Base.metadata.create_all(bind=engine)



@strawberry.type
class Book:
    id: int
    title: str
    author: str
    genre: str
    published_year: int



@strawberry.type
class Query:
    @strawberry.field
    def all_books(self) -> List[Book]:
        db = SessionLocal()
        try:
            books_db = db.query(BookModel).all()
            return [
                Book(
                    id=b.id, 
                    title=b.title, 
                    author=b.author, 
                    genre=b.genre, 
                    published_year=b.published_year
                ) for b in books_db
            ]
        finally:
            db.close()

    @strawberry.field
    def get_book(self, id: int) -> Book:
        db = SessionLocal()
        try:
            b = db.query(BookModel).filter(BookModel.id == id).first()
            if b:
                return Book(id=b.id, title=b.title, author=b.author, genre=b.genre, published_year=b.published_year)
            return None
        finally:
            db.close()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_book(self, title: str, author: str, genre: str, published_year: int) -> Book:
        db = SessionLocal()
        try:
            new_book_db = BookModel(
                title=title, 
                author=author, 
                genre=genre, 
                published_year=published_year
            )
            db.add(new_book_db)
            db.commit()
            db.refresh(new_book_db)
            

            return Book(
                id=new_book_db.id, 
                title=new_book_db.title, 
                author=new_book_db.author, 
                genre=new_book_db.genre, 
                published_year=new_book_db.published_year
            )
        finally:
            db.close()


schema = strawberry.Schema(query=Query, mutation=Mutation)