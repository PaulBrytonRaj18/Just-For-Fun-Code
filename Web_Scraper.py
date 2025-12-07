from bs4 import BeautifulSoup
import requests
import csv  


def scrape_website(url, output_file):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Extract all headings and paragraphs
    data = []
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        data.append({'type': 'heading', 'text': heading.get_text(strip=True)})
    for paragraph in soup.find_all('p'):
        data.append({'type': 'paragraph', 'text': paragraph.get_text(strip=True)})

    # Write data to CSV
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['type', 'text'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print(f"Data successfully scraped and saved to {output_file}")