"""
    API REST con Python 3 y SQLite 3
"""
from flask import Flask, jsonify, request
import controller
from database import create_tables

app = Flask(__name__)

@app.route('/users', methods=["GET"])
def get_users():
	users = controller.get_users()
	return jsonify(users)

@app.route("/user", methods=["POST"])
def insert_user():
	user_details = request.get_json()
	firstname = user_details["firstname"]
	lastname = user_details["lastname"]
	email = user_details["email"]
	password = user_details["password"]
	result = controller.insert_user(firstname, lastname, email, password)
	return jsonify(result)


@app.route("/user", methods=["PUT"])
def update_user():
    user_details = request.get_json()
    id = user_details["id"]
    firstname = user_details["firstname"]
    lastname = user_details["lastname"]
    email = user_details["email"]
    password = user_details["password"]
    result = controller.update_user(id, firstname, lastname, email, password)
    return jsonify(result)


@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    result = controller.delete_user(id)
    return jsonify(result)


@app.route("/user/<id>", methods=["GET"])
def get_user_by_id(id):
    user = controller.get_by_id(id)
    return jsonify(user)


@app.route('/books', methods=["GET"])
def get_books():
    users = controller.get_books()
    return jsonify(users)

@app.route("/book", methods=["POST"])
def insert_book():
	book_details = request.get_json()
	title = book_details["title"]
	author = book_details["author"]
	isbn = book_details["isbn"]
	publish = book_details["publish"]
	result = controller.insert_book(title, author, isbn, publish)
	return jsonify(result)

@app.route("/book", methods=["PUT"])
def update_book():
    book_details = request.get_json()
    id = book_details["id"]
    title = book_details["title"]
    author = book_details["author"]
    isbn = book_details["isbn"]
    publish = book_details["publish"]
    result = controller.update_book(id, title, author, isbn, publish)
    return jsonify(result)


@app.route("/book/<id>", methods=["DELETE"])
def delete_book(id):
    result = controller.delete_book(id)
    return jsonify(result)


@app.route("/book/<id>", methods=["GET"])
def get_book_by_id(id):
    book = controller.get_book_by_id(id)
    return jsonify(book)


@app.route('/wishes', methods=["GET"])
def get_wishes():
	users = controller.get_wishes()
	return jsonify(users)


@app.route("/wish", methods=["POST"])
def insert_wish():
	wish_details = request.get_json()
	userid = wish_details["userid"]
	bookid = wish_details["bookid"]
	result = controller.insert_wish(userid, bookid)
	return jsonify(result)

@app.route("/wish", methods=["PUT"])
def update_wish():
    wish_details = request.get_json()
    id = wish_details["id"]
    userid = wish_details["userid"]
    bookid = wish_details["bookid"]
    result = controller.update_book(id, userid, bookid)
    return jsonify(result)


@app.route("/wish/<id>", methods=["DELETE"])
def delete_wish(id):
    result = controller.delete_wish(id)
    return jsonify(result)


@app.route("/wish/<id>", methods=["GET"])
def get_wish_by_id(id):
    book = controller.get_wish_by_id(id)
    return jsonify(book)




if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)
