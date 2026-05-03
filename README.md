# 📚 Library Management System

## 👤 Author

Lorraine Hernandez

---

## 📌 Overview

The Library Management System (LMS) is a web-based application designed to replace manual, paper-based library operations. It enables efficient management of books, borrowers, and transactions while automating key processes such as due date tracking and availability updates.

This system improves accuracy, reduces human error, and enhances user experience through a clean interface and optimized backend functionality.

---

## 🚀 Features

### 🔍 Smart Book Search

* Search books by title
* Fast filtering using optimized queries

### 📖 Borrow Book Workflow

* Assign books to borrowers
* Automatically updates availability
* Prevents borrowing unavailable books

### 🔁 Return Book Functionality

* Mark books as returned
* Automatically restores availability
* Maintains data consistency

### ⏱️ Automated Due Date Tracking

* Due dates generated automatically
* Overdue books identified without manual input

### 🎨 Modern User Interface

* Responsive design using Bootstrap
* Clean and user-friendly layout

---

## 🏗️ System Architecture

Frontend (HTML, Bootstrap)
⬇
Backend (Flask - Python)
⬇
Database (SQLite with SQLAlchemy ORM)

---

## 🧩 Data Model

**Books**

* id (Primary Key)
* title
* author
* available (Boolean)

**Borrowers**

* id (Primary Key)
* name

**Transactions**

* id (Primary Key)
* book_id (Foreign Key)
* borrower_id (Foreign Key)
* due_date

---

## ⚙️ Technologies Used

* Python
* Flask
* SQLAlchemy
* SQLite
* Bootstrap
* Pytest

---

## 🧪 Testing

The system includes multiple levels of testing:

* **Unit Testing**: Validates individual components (e.g., book creation)
* **Integration Testing**: Ensures proper interaction between backend and database
* **System Testing**: Verifies full workflows such as borrowing and returning books

---

## ⚠️ Error Handling

* Input validation to prevent invalid data
* Prevents borrowing unavailable books
* User-friendly error messages
* Backend checks for data consistency

---

## ⚡ Performance Optimization

* Efficient database queries
* Lightweight SQLite database
* Optimized search functionality

---

## 🔄 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/lohernan/Library_System.git
cd Library_System
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

### 4. Seed the database (first time only)

Open in browser:

```
http://127.0.0.1:5000/seed
```

### 5. Launch the app

```
http://127.0.0.1:5000
```

---

## 🎬 Demo

The application demonstrates:

* Searching for books
* Borrowing and returning books
* Automated due date tracking
* Overdue detection

---

## 🔧 Future Improvements

* User authentication system
* Email notifications for overdue books
* Advanced filtering and sorting
* Cloud deployment for public access

---

## 📈 Maintenance & Scalability

The system is designed with modular architecture, making it easy to:

* Add new features
* Scale database functionality
* Improve performance over time

---

## 📄 License

This project is for educational purposes.
