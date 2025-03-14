import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Web_scraping"

try:
    # Send GET request to Wikipedia
    response = requests.get(url)
    response.raise_for_status() # Raise error for a bad status code

    # Parse the page with Beautiful Soup
    soup = BeautifulSoup(response.text,"html.parser")

    # Extract the title of the page
    title = soup.find("h1", id="firstHeading").text
    print(f"Page Title: {title}\n")

    # Extract the first paragraph
    first_paragraph = soup.find("p").text
    print(f"First Paragraph:\n", first_paragraph.strip())

    # Extract all links from the page
    print("\nFirst 5 Links:")
    valid_links = [link["href"] for link in soup.find_all("a", href=True) if not link["href"].startswith("#")]
    for link in valid_links[:5]:
        print(link)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
