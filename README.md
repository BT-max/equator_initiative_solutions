# Web Scraper for Nature-Based Solutions Database

This script is a web scraper that extracts data from the Nature-Based Solutions Database available on the [Equator Initiative](https://www.equatorinitiative.org/knowledge-center/nature-based-solutions-database/) website. The script is written in Python and makes use of libraries such as `requests` for making HTTP requests, `BeautifulSoup` for parsing HTML and `csv` for writing the scraped data to a CSV file.

## Requirements

- Python 3.6 or higher
- BeautifulSoup 4.9 or higher
- requests 2.25 or higher

You can install the required libraries with pip:
```
pip install beautifulsoup4 requests
```

## What Does The Script Do?

The script iterates over multiple pages of the database and extracts the following information for each item:

1. The URL of the link in the 'div' with class "cspml_thumb_container".
2. The image source (src) of the image in the 'div' with class "cspml_thumb_container".
3. The coordinates from the 'div' with class "cspml_item_pinpoint_overlay".
4. The URL and text of the link in the 'div' with class "cspml_details_title". *(Note: This information is currently not included in the script and will need to be added to scrape function)*
5. The text content in the 'div' with class "cspml_details_content". *(Note: This information is currently not included in the script and will need to be added to scrape function)*

This data is then written to a CSV file named "scraped_data.csv".

## Usage

You can run the script using Python's command-line interface:

```
python main.py
```

**Disclaimer**: Be mindful of the website's policy towards web scraping and use this script responsibly. Abusive requests can overload the server or potentially violate the site's terms of service. Please scrape respectfully, in accordance with the website's robots.txt file, and do not use this for spam or other malicious purposes.


You can refer to BeautifulSoup documentation to learn about extracting the required details: [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
