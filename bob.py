import argparse
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
import time

init(autoreset=True)

# ASCII Art
ascii_art = """
    |__| ____ _____    _______/  |________  ____   ____  
    |  |/ ___\\__  \  /  ___/\   __\_  __ \/  _ \ /  _ \ 
    |  \  \___ / __ \_\___ \  |  |  |  | \(  <_> |  <_> )
/\__|  |\___  >____  /____  > |__|  |__|   \____/ \____/ 
\______|    \/     \/     \/                                
"""

def check_args():
    parser = argparse.ArgumentParser(description="Check all links on a website for broken links.")
    parser.add_argument("url", help="The URL to start crawling")
    parser.add_argument("--timeout", type=int, default=10, help="Request timeout in seconds (default: 10)")
    parser.add_argument("--delay", type=float, default=1, help="Delay between requests in seconds (default: 1)")
    return parser.parse_args()

def get_all_links(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            return links
        else:
            print(Fore.RED + f"Failed to retrieve the page: {url} (Status code: {response.status_code})")
            return []
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Failed to retrieve the page: {url} (Error: {e})")
        return []

def check_link(url):
    try:
        response = requests.head(url, timeout=10)
        if response.status_code == 200:
            print(Fore.GREEN + f"Link is working: {url}")
        else:
            print(Fore.RED + f"Link is broken: {url} (Status code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Link is broken: {url} (Error: {e})")

def crawl_website(start_url, visited_links, delay):
    if start_url in visited_links:
        return
    visited_links.add(start_url)

    print(Fore.BLUE + f"Checking page: {start_url}")
    links = get_all_links(start_url)

    for link in links:
        if not link.startswith('http'):
            link = requests.compat.urljoin(start_url, link)
        
        if link not in visited_links:
            check_link(link)
            crawl_website(link, visited_links, delay)
        
        time.sleep(delay)

def main():
    print(Fore.BLUE + ascii_art)
    args = check_args()
    visited_links = set()
    crawl_website(args.url, visited_links, args.delay)

if __name__ == "__main__":
    main()
