from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Book, Publisher, Author, Person
from datetime import date

publishers = [
    Publisher(publisher_name="Harper Collins"),
    Publisher(publisher_name="Simon & Schuster"),
    Publisher(publisher_name="Macmillan"),
]

books = [
    Book(title="Shy",
         isbn=1435756246783,
         num_pages=476,
         publication_date=date(2005, 3, 7),
         publisher_id=1),

    Book(title="Greek lessons",
         isbn=1234327689546,
         num_pages=496,
         publication_date=date(2020, 4, 4),
         publisher_id=2),

    Book(title="Flash",
         isbn=2346543456732,
         num_pages=243,
         publication_date=date(1867, 1, 17),
         publisher_id=3),

    Book(title="Orphan",
         isbn=1232123456547,
         num_pages=1234,
         publication_date=date(2023, 7, 30),
         publisher_id=1),

    Book(title="Balloon",
         isbn=5467923076125,
         num_pages=756,
         publication_date=date(2005, 8, 4),
         publisher_id=2),
]

authors = [
    Author(author_name="Elanor Catton"),
    Author(author_name="Andrew Dales"),
    Author(author_name="Max Jones"),
    Author(author_name="Nadir Yazdi")
]

people = [
    Person(name="jonny", membership_expiry=False),
    Person(name="susan", membership_expiry=False),
    Person(name="tom", membership_expiry=False),
    Person(name="steven", membership_expiry=False),
    Person(name="arthur", membership_expiry=False),
    Person(name="charlie", membership_expiry=False)
]

books[0].authors.append(authors[0])
books[1].authors.append(authors[1])
books[2].authors.append(authors[2])
books[2].authors.append(authors[2])
books[3].authors.append(authors[1])
books[4].authors.append(authors[0])
books[4].borrowers.append(people[5])
books[3].borrowers.append(people[4])
books[3].borrowers.append(people[3])
books[0].borrowers.append(people[2])
books[2].borrowers.append(people[1])
books[2].borrowers.append(people[0])

engine = create_engine('sqlite:///library.db', echo=True)

with Session(engine) as sess:
    sess.add_all(books)
    sess.add_all(publishers)
    sess.commit()