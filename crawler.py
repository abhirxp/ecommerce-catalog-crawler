import requests
from bs4 import BeautifulSoup
import time
from database import init_db, save_book

BASE_URL = "http://books.toscrape.com/catalogue/"
START_URL = "http://books.toscrape.com/catalogue/page-1.html"

def get_soup(url):
    """Helper to get soup object from URL."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return None

def scrape_page(soup):
    """Extracts books from a single page."""
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        title = book.h3.a["title"]
        # Extract price and clean it (remove £)
        price_text = book.find("p", class_="price_color").text
        price = float(price_text.replace("£", ""))
        
        # Get Star Rating (it's a class name like "Star-Rating Three")
        rating_class = book.find("p", class_="star-rating")["class"]
        rating = rating_class[1] # "Three", "Four", etc.
        
        availability = book.find("p", class_="instock availability").text.strip()
        
        # Link to the specific book
        link = book.find("h3").find("a")["href"]
        full_url = BASE_URL + link

        # Save to SQL
        save_book(title, price, rating, availability, full_url)

def start_crawl():
    # 1. Setup Database
    init_db()
    print("--- Starting Crawler ---")

    current_url = START_URL
    page_count = 1

    while current_url:
        print(f"Scraping Page {page_count}...")
        soup = get_soup(current_url)

        if soup:
            # Step A: Scrape the books on this page
            scrape_page(soup)

            # Step B: Find the "Next" button
            next_btn = soup.find("li", class_="next")
            
            if next_btn:
                next_link = next_btn.find("a")["href"]
                current_url = BASE_URL + next_link
                page_count += 1
                time.sleep(1) # Be polite
            else:
                current_url = None # Stop the loop
        else:
            break

    print("--- Crawling Complete ---")

if __name__ == "__main__":
    start_crawl()
