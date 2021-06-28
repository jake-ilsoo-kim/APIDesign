import sqlite3
DATABASE_NAME = "/Users/jakekim/myproject/database.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname TEXT NOT NULL,
				lastname TEXT NOT NULL,
				email TEXT NOT NULL,
				password TEXT NOT NULL
            )
            """
            ,
            """
           CREATE TABLE IF NOT EXISTS book(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
           		author TEXT NOT NULL,
           		isbn TEXT NOT NULL,
           		publish DATE NOT NULL
           )
           """,
           """
           CREATE TABLE IF NOT EXISTS wishlist(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                userid INTEGER NOT NULL,
                bookid INTEGER NOT NULL,
                FOREIGN KEY(userid) REFERENCES user(id) ON UPDATE RESTRICT ON DELETE RESTRICT,
                FOREIGN KEY(bookid) REFERENCES book(id) ON UPDATE RESTRICT ON DELETE RESTRICT
           )

            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
