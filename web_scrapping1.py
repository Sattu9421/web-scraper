import requests
from bs4 import BeautifulSoup
import csv

url = 'https://blog.scrapinghub.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Change this selector based on the site's structure
articles = soup.find_all('h2', class_='post-title')

with open('blog_titles.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link'])

    for article in articles:
        title = article.get_text(strip=True)
        link = article.a['href']
        full_link = link if link.startswith('http') else f'https://blog.scrapinghub.com{link}'
        writer.writerow([title, full_link])

print("Scraping complete. Data saved to blog_titles.csv.")
