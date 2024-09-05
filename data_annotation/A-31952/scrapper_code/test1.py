import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://www.thestar.com/"

# Send request and get the HTML content
response = requests.get(url)
content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(content, "lxml")

# Find the main container that holds articles
main_container = soup.find("section", id="main-page-container")

# Initialize empty list to store articles and their content
scraped_articles = []

# Check if the main container exists
if main_container:
    # Find all articles within the container
    articles = main_container.find_all("div", class_="col-md-12")

    # Loop through each article and extract title and content
    for article in articles:
        # Extract title - Adjust the class or tag according to the website's structure
        title_tag = article.find("h3")  # Adjust based on the actual tag used for titles
        if title_tag:
            title = title_tag.text.strip()
        else:
            title = "No title found"

        # Extract content - Adjust the class or tag according to the website's structure
        content_body = article.find("div", class_="c-article__content")
        if content_body:
            content_text = content_body.text.strip()
        else:
            content_text = "No content found"

        # Append article and content to the list
        scraped_articles.append({"title": title, "content": content_text})

# Print or store the scraped articles
print(f"Scraped {len(scraped_articles)} articles:")
for article in scraped_articles:
    print(f"\nTitle: {article['title']}")
    print(f"Content: {article['content']}")
