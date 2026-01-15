import sqlite3

# Connect to the database
conn = sqlite3.connect('books.db')
c = conn.cursor()

# 1. Count how many books we found
c.execute("SELECT COUNT(*) FROM books")
count = c.fetchone()[0]
print(f"Total Books Scraped: {count}")

# 2. Show the top 5 most expensive books
print("\n--- Top 5 Most Expensive Books ---")
c.execute("SELECT title, price FROM books ORDER BY price DESC LIMIT 5")
for row in c.fetchall():
    print(f"£{row[1]} - {row[0]}")

# 3. Show a random sample of 3 books
print("\n--- Random Sample ---")
c.execute("SELECT title, rating, availability FROM books ORDER BY RANDOM() LIMIT 3")
for row in c.fetchall():
    print(row)

conn.close()
