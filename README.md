# BOB

## Description
This Python script is a tool for crawling a website and checking all its links (both internal and external) to identify broken links. It recursively follows links on the site, ensuring that only unique links are checked to avoid duplication or infinite loops. The tool outputs the status of each link directly in the terminal.

## Features
- Crawls an entire website starting from a given URL.
- Identifies broken links with HTTP status codes or error messages.
- Handles both internal and external links.
- Avoids revisiting already-checked links.
- Configurable timeout and delay between requests.

## Dependencies
The script uses the following Python libraries:

- `argparse`: For parsing command-line arguments.
- `requests`: For making HTTP requests and checking link statuses.
- `bs4` (BeautifulSoup): For parsing HTML and extracting links.
- `colorama`: For color-coded output in the terminal.

You can install these dependencies with the provided `requirements.txt` file.

## Installation
1. Clone or download this repository.
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script with the following command:
```bash
python bob.py <URL>
```

### Example
```bash
python bob.py https://example.com
```

### Optional Parameters
- `--timeout`: Set the request timeout in seconds (default: 10).
  ```bash
  python bob.py https://example.com --timeout 15
  ```
- `--delay`: Set the delay between requests in seconds (default: 1).
  ```bash
  python bob.py https://example.com --delay 2
  ```

## How It Works
1. The script starts by fetching the HTML content of the given URL.
2. It extracts all the links (`<a>` tags with `href` attributes) from the page.
3. Links are normalized to handle relative paths.
4. Each link is checked via an HTTP request to determine its status.
5. The script recursively crawls internal links until all reachable links have been checked.

## Output
- **Green**: Links that are functional (status code 200).
- **Red**: Links that are broken (non-200 status codes or request errors).
- Errors and HTTP status codes are displayed for broken links.

## Limitations
- The script does not respect `robots.txt`. Ensure compliance before running the tool on external websites.
- It does not handle JavaScript-generated links.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

### Created by João Castro.
