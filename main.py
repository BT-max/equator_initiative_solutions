import csv

import requests
from bs4 import BeautifulSoup

URL = 'https://www.equatorinitiative.org/knowledge-center/nature-based-solutions-database/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.93 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8',
    'referer': 'https://www.equatorinitiative.org/',
    'Accept-Language': 'en-US,en;q=0.5'
}


def get_html(url):
    """
    Sends a GET request to the provided URL and returns the response.
    """
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
    except (requests.RequestException, ValueError):
        print("Network error")
        return None
    return response.text


def scrape(soup):
    """
    Scrape required data from the BeautifulSoup object and return it as a list of dictionaries.
    """
    data = []
    for div in soup.find_all('div',
                             class_='cspml_item cspm-col-lg-12 cspm-col-xs-12 cspm-col-sm-12 cspm-col-md-12 '
                                    'cspm_border_shadow cspm_border_radius'):
        item_data = {}
        thumb_container = div.find('div',
                                   class_='cspml_thumb_container cspm-col-lg-12 cspm-col-xs-12 cspm-col-sm-12 '
                                          'cspm-col-md-12 no-padding')
        if thumb_container:
            link = thumb_container.find('a')
            if link:
                item_data['link_url'] = link['href']
            img = thumb_container.find('img', class_='thumb img-responsive')
            if img:
                item_data['img_src'] = img['src']
            pinpoint_overlay = thumb_container.find('div',
                                                    class_='cspml_item_pinpoint_overlay cspml_fire_pinpoint '
                                                           'cspm_bg_rgb_hover')
            if pinpoint_overlay:
                item_data['coordinates'] = pinpoint_overlay['data-coords']
        data.append(item_data)
    return data


def write_to_csv(data):
    """
    Write the provided data to a CSV file.
    """
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['link_url', 'img_src', 'coordinates']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow(item)


def main():
    html = get_html(URL)
    if not html:
        return

    soup = BeautifulSoup(html, 'html.parser')

    # Get total number of pages from the pagination section
    pagination = soup.find(
        'div',
        class_='cspml_pagination_map3144 cspm-col-lg-12 cspm-col-md-12 cspm-col-sm-12 cspm-col-xs-12'
    )
    last_page_url = pagination.find_all('a', class_='page-numbers')[-2]['href']
    total_pages = int(last_page_url.split('/page/')[1].split('/')[0])

    data = []

    for page in range(1, total_pages + 1):
        page_url = f"{URL}page/{page}/?paginate=true"
        html = get_html(page_url)
        if not html:
            continue
        soup = BeautifulSoup(html, 'html.parser')
        page_data = scrape(soup)
        data.extend(page_data)

    write_to_csv(data)


if __name__ == '__main__':
    main()
