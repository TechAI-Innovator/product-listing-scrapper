# Saves to SQLite, JSON and CSV depending on the CLI to offer flexibility


import json
import csv
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(String)
    rating = Column(Integer)
    detail_url = Column(String)

def save_to_json(data, filename="output.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"[+] Saved {len(data)} records to {filename}")

def save_to_csv(data, filename="output.csv"):
    if not data:
        print("[-] No data to save.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"[+] Saved {len(data)} records to {filename}")

def save_to_sqlite(data, db_name="books.db"):
    if not data:
        print("[-] No data to save.")
        return

    engine = create_engine(f"sqlite:///{db_name}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for item in data:
        book = Book(
            title=item["title"],
            price=item["price"],
            rating=item["rating"],
            detail_url=item["detail_url"]
        )
        session.add(book)

    session.commit()
    session.close()
    print(f"[+] Saved {len(data)} records to {db_name}")

def save_data(data, format):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if format == "json":
        save_to_json(data, f"output_{timestamp}.json")
    elif format == "csv":
        save_to_csv(data, f"output_{timestamp}.csv")
    elif format == "sqlite":
        save_to_sqlite(data, f"books_{timestamp}.db")
    else:
        print("[-] Unknown format:", format)
