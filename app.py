from flask import Flask, render_template, request, redirect
from models import db, Book, Borrower, Transaction
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# Create DB
with app.app_context():
    db.create_all()

# Home Page
@app.route('/')
def index():
    query = request.args.get('search')
    if query:
        books = Book.query.filter(Book.title.contains(query)).all()
    else:
        books = Book.query.all()
    return render_template('index.html', books=books)

# Borrow Book
@app.route('/borrow/<int:book_id>', methods=['GET', 'POST'])
def borrow(book_id):
    book = Book.query.get(book_id)

    if request.method == 'POST':
        name = request.form['name']

        if not book.available:
            return "Book not available!"

        borrower = Borrower(name=name)
        db.session.add(borrower)
        db.session.commit()

        transaction = Transaction(book_id=book.id, borrower_id=borrower.id)
        db.session.add(transaction)

        book.available = False
        db.session.commit()

        return redirect('/')

    return render_template('borrow.html', book=book)

# Overdue Checker (AUTOMATION FEATURE)
@app.route('/overdue')
def overdue():
    from datetime import datetime

    today = datetime.now()
    overdue_records = Transaction.query.filter(Transaction.due_date < today).all()

    html = """
    <h2 style='text-align:center;'>⚠️ Overdue Books</h2>
    <ul style='max-width:600px;margin:auto;'>
    """

    for record in overdue_records:
        html += f"<li>Book ID: {record.book_id} | Due: {record.due_date.strftime('%Y-%m-%d')}</li>"

    html += "</ul>"

    if not overdue_records:
        html += "<p style='text-align:center;'>No overdue books 🎉</p>"

    return html

# Seed Data (run once)
@app.route('/seed')
def seed():
    book1 = Book(title="Python Basics", author="John Doe")
    book2 = Book(title="Flask Guide", author="Jane Smith")

    db.session.add_all([book1, book2])
    db.session.commit()
    return "Database seeded!"


@app.route('/return/<int:book_id>')
def return_book(book_id):
    book = Book.query.get_or_404(book_id)

    transaction = Transaction.query.filter_by(book_id=book.id)\
        .order_by(Transaction.id.desc()).first()

    if transaction:
        db.session.delete(transaction)

    book.available = True
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)