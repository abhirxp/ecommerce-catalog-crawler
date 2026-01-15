import sqlite3

def init_db():
    """Creates the database and table if they don't exist."""
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            price REAL,
            rating TEXT,
            availability TEXT,
            url TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_book(title, price, rating, availability, url):
    """Inserts a single book into the database."""
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO books (title, price, rating, availability, url)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, price, rating, availability, url))
    conn.commit()
    conn.close()
    print(f"   [SAVED] {title}")
