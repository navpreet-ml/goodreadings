import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

if not "postgres://mzrdgduspbgunk:b676b0b49656b5dc0250561643021467b6c888609317180fdde2c5dd8acaa9c4@ec2-35-174-127-63.compute-1.amazonaws.com:5432/d128b3h64d9cli":
    raise RuntimeError("DATABASE_URL is not set")

engine= create_engine("postgres://mzrdgduspbgunk:b676b0b49656b5dc0250561643021467b6c888609317180fdde2c5dd8acaa9c4@ec2-35-174-127-63.compute-1.amazonaws.com:5432/d128b3h64d9cli")
db =scoped_session(sessionmaker(bind=engine))

def main():
    db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, password VARCHAR NOT NULL)")
    db.execute("CREATE TABLE reviews (isbn VARCHAR NOT NULL,review VARCHAR NOT NULL, rating INTEGER NOT NULL,username VARCHAR NOT NULL)")
    db.execute("CREATE TABLE books (isbn VARCHAR PRIMARY KEY,title VARCHAR NOT NULL,author VARCHAR NOT NULL,year VARCHAR NOT NULL)")
    f=open("books.csv")
    reader =csv.reader(f)
    for isbn,title,author,year in reader:
        if year == "year":
            print('skipped first line')
        else:    
            db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:a,:b,:c,:d)",{"a":isbn,"b":title,"c":author,"d":year})
        
    print("done")            
    db.commit()    

if __name__ == "__main__":
    main()