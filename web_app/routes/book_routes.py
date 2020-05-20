from flask import Blueprint, jsonify, request, render_template, flash, redirect

from web_app.models import Book, db, parse_records

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
@book_routes.route("/books_endpoint")
def list_books():
    books = Book.query.all()
    books_response = parse_records(books)
    return jsonify(books_response)

@book_routes.route("/books")
def list_books_for_humans():

    book_records = Book.query.all()
    print(book_records)

    return render_template("books.html", message="Here's some books", books=book_records)

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))

    new_book = Book(title=request.form["book_title"], author_id=request.form["author_name"])
    db.session.add(new_book)
    db.session.commit()

    # return jsonify({
    #     "message": "BOOK CREATED OK",
    #     "book": dict(request.form)
    # })
    flash(f"Book '{new_book.title}' created successfully!", "success")
    return redirect("/books")