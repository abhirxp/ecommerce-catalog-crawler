# 📚 E-commerce Catalog Crawler (SQLite Integration)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Database](https://img.shields.io/badge/Database-SQLite-green)
![Type](https://img.shields.io/badge/Type-Crawler-orange)

## 📋 Project Overview
A sophisticated web crawler built to navigate multi-page e-commerce sites. Unlike simple scrapers, this bot handles **pagination** automatically, traversing the entire "Books to Scrape" catalog to extract product details and persist them into a structured **relational database (SQL)**.

**Key Capabilities:**
* **Deep Crawling:** Navigates through 50+ pages automatically using "Next" button logic.
* **Structured Storage:** Saves data directly to SQLite rather than flat CSV files, enabling complex querying.
* **Resilience:** Includes error handling for network timeouts and missing DOM elements.

## ⚙️ How It Works
1.  **Initialization:** Checks for an existing `books.db` and creates the schema if missing.
2.  **Crawl Loop:**
    * Scrapes all book data (Title, Price, Star Rating, Availability) from the current page.
    * Inserts data transactionally into the database.
    * Identifies the "Next" pagination link.
    * Repeats until no "Next" link is found.

## 🛠️ Technical Stack
* **Requests:** HTTP Session management.
* **BeautifulSoup4:** HTML Parsing and DOM traversal.
* **SQLite3:** Local relational database management.

## 🚀 Installation & Usage

1.  **Clone the repo**
    ```bash
    git clone [https://github.com/yourusername/ecommerce-catalog-crawler.git](https://github.com/yourusername/ecommerce-catalog-crawler.git)
    cd ecommerce-catalog-crawler
    ```

2.  **Install Requirements**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Crawler**
    ```bash
    python crawler.py
    ```
    *The script will print real-time logs as it scrapes each page.*

4.  **View the Data**
    You can use any SQLite viewer or run the included `viewer.py` script (if applicable) to query the `books.db` file.

## 📊 Database Schema
| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | INTEGER PK | Auto-incrementing unique ID |
| `title` | TEXT | Book Title |
| `price` | REAL | Price in GBP (£) |
| `rating` | TEXT | Star rating (One, Two, Three, etc.) |
| `availability`| TEXT | Stock status |
| `url` | TEXT | Direct link to product |

---
*Developed by [Your Name] - Open for Data Mining & Extraction Projects.*
