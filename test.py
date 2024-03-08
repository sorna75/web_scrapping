import requests
from bs4 import BeautifulSoup

# Make a request to the webpage
url = 'https://markets.ft.com/data/world/countries/india'
response =requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'lxml')

    # Provide the full XPath of the element you want to extract
    full_xpath = '/html/body/div[3]/div[1]/section[2]/div[3]/div/div[2]/div[1]'

    # Use the find method with the full XPath
    element = soup.find('xpath', full_xpath)
    print(element)
    article_titles = soup.find_all('div')
    for title in article_titles:
        print(title.text)
    # Check if the element is found
    if element:
        # Print the text content of the element
        print(element.text)
    else:
        print(f"Element not found with XPath: {full_xpath}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


