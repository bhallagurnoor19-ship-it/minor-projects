import re
import requests
import pandas as pd
from bs4 import BeautifulSoup


START_URL = "http://books.toscrape.com/catalogue/page-1.html"


def get_rating(rating_class):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(rating_class, 0)


def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        response.encoding = "utf-8"
    except requests.RequestException as e:
        print(f"Error fetching {url}")
        print(e)
        return [], None

    soup = BeautifulSoup(response.text, "html.parser")

    books = []

    articles = soup.find_all("article", class_="product_pod")

    for article in articles:

        title = article.h3.a["title"]

        price_text = article.find("p", class_="price_color").get_text(strip=True)

        match = re.search(r"\d+\.\d+", price_text)

        price = float(match.group()) if match else 0.0

        rating_class = article.find("p", class_="star-rating")["class"][1]

        rating = get_rating(rating_class)

        books.append(
            {
                "Title": title,
                "Price (£)": price,
                "Rating": rating
            }
        )

    next_button = soup.find("li", class_="next")

    if next_button:
        next_page = next_button.find("a")["href"]

        current_url = url.rsplit("/", 1)[0]

        next_url = current_url + "/" + next_page
    else:
        next_url = None

    return books, next_url


def main():

    all_books = []

    url = START_URL

    while url:

        print(f"Scraping: {url}")

        books, url = scrape_page(url)

        all_books.extend(books)

    df = pd.DataFrame(all_books)

    df.to_csv("books.csv", index=False)

    print("\nScraping completed successfully.")
    print(f"Total books scraped: {len(df)}")
    print("Data saved as books.csv")


if __name__ == "__main__":
    main()