import requests
from bs4 import BeautifulSoup
def simple_web_crawler(url, max_depth=2):
    visited_urls = set()
    def crawl(url,depth):
        if depth > max_depth or url in visited_urls:
            return
        print(f"Crawling: {url}")
        try:
            response = requests.get(url)
            visited_urls.add(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.title.string.strip() if soup.title else 'No title found'
                print(f"Page Title: {title}")
                for link in soup.find_all('a', href=True):
                    next_url = link['href']
                    crawl(next_url, depth + 1)
        except Exception as e:
            print(f"Error crawling {url}: {e}")
    crawl(url, depth=1)
if __name__ == "__main__":
    start_url = "https://example.com"
    simple_web_crawler(start_url)
