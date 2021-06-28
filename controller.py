from database import get_db


def insert_user(firstname, lastname, email, password):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO user(firstname, lastname, email, password) VALUES (?, ?, ?, ?)"
    cursor.execute(statement, [firstname, lastname, email, password])
    db.commit()
    return True

def update_user(id, firstname, lastname, email, password):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE user SET firstname = ?, lastname = ?, email = ? , password= ? WHERE id = ?"
    cursor.execute(statement, [firstname, lastname, email, password, id])
    db.commit()
    return True

def delete_user(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM user WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT firstname, lastname, email, password FROM user WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_users():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, firstname, lastname, email, password FROM user"
    cursor.execute(query)
    return cursor.fetchall()


def get_books():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, title, author, isbn, publish FROM book"
    cursor.execute(query)
    return cursor.fetchall()

def insert_book(title, author, isbn, publish):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO book(title, author, isbn, publish) VALUES (?, ?, ?, ?)"
    cursor.execute(statement, [title, author, isbn, publish])
    db.commit()
    return True

def update_book(id, title, author, isbn, publish):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE book SET title = ?, author = ?, isbn = ? , publish= ? WHERE id = ?"
    cursor.execute(statement, [title, author, isbn, publish, id])
    db.commit()
    return True

def delete_book(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM book WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True

def get_book_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT title, author, isbn, publish FROM book WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def get_wishes():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, userid, bookid FROM wishlist"
    cursor.execute(query)
    return cursor.fetchall()

def insert_wish(userid, bookid):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO wishlist(userid, bookid) VALUES (?, ?)"
    cursor.execute(statement, [userid, bookid])
    db.commit()
    return True

def update_wish(id, userid, bookid):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE wishlist SET userid = ?, bookid = ? WHERE id = ?"
    cursor.execute(statement, [userid, bookid, id])
    db.commit()
    return True

def delete_wish(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM wishlist WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True

def get_wish_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT userid, bookid FROM wishlist WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()
